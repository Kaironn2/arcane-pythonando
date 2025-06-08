from datetime import datetime, timedelta
from typing import List

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup
from django.core.cache import cache
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from .models import Trainning
from .wrapper_evolutionapi import SendMessage


def html_to_rag_text(html_str: str) -> str:
    soup = BeautifulSoup(html_str, 'html.parser')
    final_text = []

    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li']):
        text = tag.get_text(strip=True)

        if not text:
            continue

        h_tags = ['h1', 'h2', 'h3']
        if tag.name in h_tags:
            formated_text = f'\n\n### {text.upper()}'
        elif tag.name == 'li':
            formated_text = f' - {text}'
        else:
            formated_text = text

        final_text.append(formated_text)

    return '\n'.join(final_text).strip()


def documents_generate(instance: Trainning) -> List[Document]:
    documents = []
    if instance.document:
        extension = instance.document.name.split('.')[-1].lower()
        if extension == 'pdf':
            loader = PyPDFLoader(instance.document.path)
            pdf_doc = loader.load()
            for doc in pdf_doc:
                doc.metadata['url'] = instance.document.url
            documents += pdf_doc

    if instance.content:
        document = Document(page_content=instance.content)
        documents.append(document)

    if instance.site:
        site_url = (
            instance.site if instance.site.startswith('https://')
            else f'https://{instance.site}'
        )
        content = requests.get(site_url, timeout=10).text
        content = html_to_rag_text(content)
        documents.append(Document(page_content=content))

    return documents


scheduler = BackgroundScheduler()
scheduler.start()


def send_message_response(phone):
    messages = cache.get(f'wa_buffer_{phone}', [])
    if messages:
        question = '\n'.join(messages)
        embeddings = OpenAIEmbeddings()
        vectordb = FAISS.load_local(
            'faiss_db', embeddings, allow_dangerous_deserialization=True
        )
        docs = vectordb.similarity_search(question, k=5)
        context = '\n\n'.join([doc.page_content for doc in docs])

        prompt = f"""
                Você é um assistente virtual e deve responder com precisão as
                perguntas sobre uma empresa.\n\n{context}
                """
        messages = [
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': question.question}
        ]

        llm = ChatOpenAI(
            model_name='gpt-4o-mini',
            temperature=0,
        )

        response = llm.invoke(messages).content

        SendMessage().send_message(
            'arcane', {'number': phone, 'textMessage': {'text': response}}
        )

        cache.delete(f'wa_buffer_{phone}')
        cache.delete(f'wa_timer_{phone}')


def sched_message_response(phone):
    if not cache.get(f'wa_timer_{phone}'):
        print('Agendando')
        scheduler.add_job(
           send_message_response,
           'date',
           run_date=datetime.now() + timedelta(seconds=15),
           kwargs={'phone': phone},
           misfire_grace_time=60
        )
        cache.set(f'wa_timer_{phone}', True, timeout=60)

from typing import List

import requests
from bs4 import BeautifulSoup
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyPDFLoader


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


def documents_generate(instance) -> List[Document]:
    documents = []
    if instance.document:
        extensao = instance.document.name.split('.')[-1].lower()
        if extensao == 'pdf':
            loader = PyPDFLoader(instance.document.path)
            pdf_doc = loader.load()
            documents += pdf_doc

    if instance.content:
        documents.append(Document(page_content=instance.content))
    if instance.site:
        site_url = (
            instance.site if instance.site.startswith('https://')
            else f'https://{instance.site}'
        )
        content = requests.get(site_url, timeout=10).text
        content = html_to_rag_text(content)
        documents.append(Document(page_content=content))

    return documents

import os

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from .models import Trainning
from .utils import documents_generate


@receiver(post_save, sender=Trainning)
def signals_treinamento_ia(sender, instance, created, **kwargs):
    if created:
        async_task(task_ai_trainning, instance.id)


def task_ai_trainning(instance_id):
    instance = Trainning.objects.get(id=instance_id)
    documents = documents_generate(instance)
    if not documents:
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

    db_path = str(settings.BASE_DIR / 'faiss_db')
    if os.path.exists(db_path):
        vectordb = FAISS.load_local(
            db_path, embeddings, allow_dangerous_deserialization=True
        )
        vectordb.add_documents(chunks)
    else:
        vectordb = FAISS.from_documents(chunks, embeddings)
        vectordb.save_local(db_path)

from pathlib import Path

from django.conf import settings
from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    JsonResponse,
    StreamingHttpResponse,
)
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django_q.tasks import Task
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from rolepermissions.checkers import has_permission

from .models import Question, Trainning, TrainningData


def ai_trainning(request: HttpRequest) -> HttpResponse:
    if not has_permission(request.user, 'ai_trainning'):
        raise Http404()
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'ai-trainning.html', {'tasks': tasks})
    elif request.method == 'POST':
        site = request.POST.get('site')
        content = request.POST.get('content')
        document = request.FILES.get('document')

        trainning = Trainning(
            site=site,
            content=content,
            document=document,
        )
        trainning.save()

        return redirect('ai_trainning')


@csrf_exempt
def chat(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'chat.html')
    elif request.method == 'POST':
        user_question = request.POST.get('question')

        question = Question(
            question=user_question
        )
        question.save()

        return JsonResponse({'id': question.id})


@csrf_exempt
def stream_response(request: HttpRequest) -> StreamingHttpResponse:
    id_question = request.POST.get('id_question')
    question = Question.objects.get(id=id_question)

    def stream_generator():
        embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        vector_db = FAISS.load_local(
            'faiss_db', embeddings, allow_dangerous_deserialization=True
        )

        docs = vector_db.similarity_search(question.question, k=5)
        for doc in docs:
            dt = TrainningData.objects.create(
                metadata=doc.metadata,
                text=doc.page_content,
            )
            question.trainning_data.add(dt)

        context = '\n\n'.join([
            f'Material: {Path(
                doc.metadata.get('source', 'Desconhecido')
            ).name}\n{doc.page_content}'
            for doc in docs
        ])

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
            streaming=True,
            temperature=0,
            openai_api_key=settings.OPENAI_API_KEY
        )

        for chunk in llm.stream(messages):
            token = chunk.content
            if token:
                yield token

    return StreamingHttpResponse(
        stream_generator(), content_type='text/plain; charset=utf-8'
    )


def info_source(request: HttpRequest, id: int) -> HttpResponse:
    question = Question.objects.get(id=id)
    for i in question.trainning_data.all():
        print(i.metadata)
        print(i.text)
        print('---')
    print(question.question)

    return render(request, 'info-source.html', {'question': question})

from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django_q.tasks import Task
from rolepermissions.checkers import has_permission

from .models import Question, Trainning


def ai_trainning(request: HttpRequest) -> HttpResponse:
    if not has_permission(request.user, 'ai_trainning'):
        raise Http404()
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'ai_trainning.html', {'tasks': tasks})
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
def chat(request):
    if request.method == 'GET':
        return render(request, 'chat.html')
    elif request.method == 'POST':
        user_question = request.POST.get('question')

        question = Question(
            question=user_question
        )
        question.save()

        return JsonResponse({'id': question.id})

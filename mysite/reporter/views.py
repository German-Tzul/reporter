from django.shortcuts import render

from .models import Reporter

def index(request):
    latest_question_list = Reporter.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'reporter/index.html', context)
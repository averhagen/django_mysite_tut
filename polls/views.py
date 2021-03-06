from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_response = Question.objects.order_by('-pub_date')
    context = {
        'latest_question_list': latest_question_response
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at questions %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You're voting on question %s"
    return HttpResponse(response % question_id)
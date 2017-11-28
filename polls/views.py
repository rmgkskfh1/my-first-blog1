from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def index(request):
    #예 1번- 단순 텍스트
    #return HttpResponse("Hello, world. You're at the polls index.")
    #예 2번- CRM 결과를 가져와서 화면에 ','로 붙여 보여준다.
    # latest_question_list = Question.objects.order_by('pub_date')[:5]
    # output = ','.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)
    #예 3번  - 템플릿을 적용한다.----------------
    #latest_question_list= Question.objects.order_by('pub_date')[:5]
    # template = loader.get_template('polls/index_html')
    # context ={
    #     'latest_question_list':latest_question_list.
    # }
    # return HttpResponse(tmplate.render(context,request))
    # 예4번은 3번 방식의 개선(간편) 버전
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
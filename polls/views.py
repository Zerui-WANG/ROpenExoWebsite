from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def storyboard(request):
    storyboards = [
        {
            'title' : 'Storyboard_1',
            'description' : 'Storyboard_Beneficaire_1',
            'url' : 'storyboard/Storyboard_-_Beneficaire_1.jpg',
        },
        {
            'title' : 'Storyboard_2',
            'description' : 'Storyboard_Beneficaire_2',
            'url' : 'storyboard/Storyboard_-_Beneficaire_2.jpg',
        },
        {
            'title' : 'Storyboard_3',
            'description' : 'Storyboard_Beneficaire_3',
            'url' : 'storyboard/Storyboard_-_Beneficaire_3.jpg',
        },
        {
            'title' : 'Storyboard_4',
            'description' : 'Storyboard_Parent',
            'url' : 'storyboard/Storyboard_-_Parent.jpg',
        },
        {
            'title' : 'Storyboard_5',
            'description' : 'Storyboard_Personel_soignant',
            'url' : 'storyboard/Storyboard_-_Personnel_soignant.png',
        },
    ]
    context = {'storyboards': storyboards}
    return render(request, 'polls/storyboard.html', context)

def aPropos(request):
    return render(request, 'polls/aPropos.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', 
            {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

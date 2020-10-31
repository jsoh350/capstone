from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Sentence, Record


def results(request, sentence):
    if request.method == 'POST':
            sentence = Sentence()
            sentence.user_email=request.POST['user_email']
            sentence.input_type=request.POST['input_type']
            sentence.typing_speed=request.POST['typing_speed']
            sentence.total_time=float(request.POST['total_time'])
            sentence.total_move=request.POST['total_move']
            sentence.accuracy=float(request.POST['accuracy'])
            sentence.erased_letter=request.POST['erased_letter']
            sentence.score=request.POST['score']
            sentence.save()
    return render(request, 'capstone/results.html')

def detail(request, sentence):
    if request.method == 'POST':
        record = Record()
        record.user_email = request.POST['user_email']
        record.avg_speed = request.POST['avg_speed']
        record.avg_accuracy = request.POST['avg_accuracy']
        record.input_type = request.POST['input_type']
        record.total_score = request.POST['total_score']
    return render(request, 'capstone/detail.html')
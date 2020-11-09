import urllib

from django.contrib.postgres import serializers
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Sentence, Record

@csrf_exempt
def results(request, sentence):
    if request.method == 'POST':
            sentence = Sentence()
            sentence.user_email = request.POST['user_email']
            sentence.input_type = request.POST['input_type']
            sentence.typing_speed = request.POST['typing_speed']
            sentence.total_time = float(request.POST['total_time'])
            sentence.total_move = request.POST['total_move']
            sentence.accuracy = float(request.POST['accuracy'])
            sentence.erased_letter = request.POST['erased_letter']
            sentence.score = request.POST['score']
            sentence.save()
            return HttpResponse()

@csrf_exempt
def complete(request, sentence):
    if request.method == 'POST':
        record = Record.objects.all()
        record.user_email = request.POST['user_email']
        record.avg_speed = request.POST['avg_speed']
        record.avg_accuracy = request.POST['avg_accuracy']
        record.input_type = request.POST['input_type']
        record.total_score = request.POST['total_score']
    return HttpResponse()

@csrf_exempt
def leaderboard(request, input_type):
    if request.method == 'GET':
        lb = Record.objects.all()

        lb1 = lb.filter(input_type)
        lb1 = lb1.order_by('total_score')
        lb1 = lb1[:5]
        for model_instance in lb1:
         str1 = lb1[0].user_email[:3] + lb1[0].avg_speed + lb1[0].avg_accuracy + lb1[0].input_type + lb1[0].total_score
         str2 = lb1[1].user_email[:3] + lb1[1].avg_speed + lb1[1].avg_accuracy + lb1[1].input_type + lb1[1].total_score
         str3 = lb1[2].user_email[:3] + lb1[2].avg_speed + lb1[2].avg_accuracy + lb1[2].input_type + lb1[2].total_score
         str4 = lb1[3].user_email[:3] + lb1[3].avg_speed + lb1[3].avg_accuracy + lb1[3].input_type + lb1[3].total_score
         str5 = lb1[4].user_email[:3] + lb1[4].avg_speed + lb1[4].avg_accuracy + lb1[4].input_type + lb1[4].total_score
        return HttpResponse(str(str1), str(str2), str(str3), str(str4), str(str5))

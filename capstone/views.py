from django.http import HttpResponse
from .models import Sentence, Record

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

def complete(request, sentence):
    if request.method == 'POST':
        record = Record.objects.all()
        record.user_email = request.POST['user_email']
        record.avg_speed = request.POST['avg_speed']
        record.avg_accuracy = request.POST['avg_accuracy']
        record.input_type = request.POST['input_type']
        record.total_score = request.POST['total_score']
    return HttpResponse()

def leaderboard(request, input_type):
    if request.method == 'GET':
        lb = Record.objects.all()

        lb1 = lb.filter(input_type)
        lb1 = lb1.order_by('total_score')
        lb1 = lb1[:5]
        for model_instance in lb1:
            print(lb1.user_email[:3])
            print(lb1.total_score)
            
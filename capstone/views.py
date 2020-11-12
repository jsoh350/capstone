import urllib
from django.views.decorators.csrf import csrf_exempt
from django.contrib.postgres import serializers
from django.http import HttpResponse, Http404
from .models import Sentence, Record

@csrf_exempt
def results(request, sentence):
    if request.method == 'POST':
            record = Sentence()
            record.user_email = request.POST['user_email']
            record.input_type = request.POST['input_type']
            record.typing_speed = request.POST['typing_speed']
            record.total_time = float(request.POST['total_time'])
            record.total_move = float(request.POST['total_move'])
            record.accuracy = float(request.POST['accuracy'])
            record.erased_letter = request.POST['erased_letter']
            record.score = request.POST['score']
            record.target=sentence
            record.save()
            return HttpResponse()

@csrf_exempt
def complete(request):
    if request.method == 'POST':
        em=request.POST['user_email']
        record = Record.objects.filter(user_email=em)
        if len(record)!=0:
            record[0].delete()
        rec=Record()
        rec.user_email = em
        recent=Sentence.objects.filter(user_email=em).order_by('-id')[:15]
        spd=0
        acc=0
        rec.total_score = 0
        for itm in recent:
           spd+=itm.typing_speed
           acc+=itm.accuracy
           rec.total_score+=itm.score
        record.avg_speed = spd/15
        record.avg_accuracy = acc/15
        record.save()
        return HttpResponse()
    
@csrf_exempt
def leaderboard(request, input_type):
    if request.method == 'POST':
        lb = Record.objects.filter(input_type=input_type).order_by('total_score')
        res="순위\t이메일\t속도\t정확도\t총점\n"
        rank=1
        if len(lb)>=5:
            lb=lb[:5]
        for line in lb:
            res+=str(rank)+'\t'+\
                  line.user_email[:3]+'\t'\
                  +str(line.avg_speed)+'\t'\
                  +str(line.avg_accuracy)+'\t'\
                  +str(line.total_score)+'\n'
            rank+=1
        em = request.POST['email']
        lb = Record.objects.filter(input_type=input_type).order_by('total_score')
        for i in range(len(lb)):
            if lb[i].user_email==em:
                res+='\n'+str(i+1)+lb[i].user_email+'\t'\
                      +str(lb[i].avg_speed)+'\t'\
                      +str(lb[i].avg_accuracy)+'\t'\
                      +str(lb[i].total_score)
                break
        return HttpResponse(res)
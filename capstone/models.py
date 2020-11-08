from django.db import models
from django.db.models import Sum, Avg


class Sentence(models.Model):
    user_email = models.CharField(max_length=200)
    input_type = models.IntegerField(default=0)
    typing_speed = models.IntegerField(default=0)
    total_time = models.FloatField()
    total_move = models.IntegerField()
    accuracy = models.FloatField(default=0)
    erased_letter = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

class Record(models.Model):
    user_email = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    avg_speed = models.FloatField(Sentence.objects.aggregate(Avg('typinng_speed')))
    avg_accuracy = models.FloatField(Sentence.objects.aggregate(Avg('accuracy')))
    input_type = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    total_score = models.IntegerField(Sentence.objects.aggregate(Sum('Score')))

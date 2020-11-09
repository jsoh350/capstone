from django.db import models


class Sentence(models.Model):
    user_email = models.CharField(max_length=200)
    input_type = models.IntegerField(default=0)
    typing_speed = models.IntegerField(default=0)
    total_move = models.FloatField(default=0)
    accuracy = models.FloatField(default=0)
    erased_letter = models.CharField(max_length=10)
    score = models.IntegerField(default=0)

class Record(models.Model):
    user_email = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    avg_speed = models.FloatField(default=0)
    avg_accuracy = models.FloatField
    input_type = models.IntegerField
    total_score = models.IntegerField(default=0)

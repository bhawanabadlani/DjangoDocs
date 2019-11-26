from django.db import models

def Question(models.Model):
    question_text = models.Charfield(max_length=200)
    pub_date = models.DateTimeField('date published')

def Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.Charfield(max_length=0)
    votes = models.IntegerField(default=0)
# Create your models here.

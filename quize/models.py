from django.db import models
from django.utils import timezone


# Create your models here.


class relation(models.Model):
    name_quize = models.TextField()
    major = models.TextField()
    publish = models.DateTimeField(default=timezone.now)


class questions(models.Model):
    quize = models.ForeignKey(relation, on_delete=models.CASCADE, related_name="relative")
    question = models.CharField(max_length=1000)
    right_answer = models.IntegerField()

    def __str__(self):
        return self.question


class answers(models.Model):
    question_id = models.ForeignKey(questions, on_delete=models.CASCADE, related_name="related_question")
    answer = models.TextField(max_length=500)

    def __str__(self):
        return str(self.question_id)

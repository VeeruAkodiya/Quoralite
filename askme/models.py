from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerd_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)


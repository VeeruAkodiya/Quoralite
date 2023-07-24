from django import forms
from askme.models import Question, Answer, Like


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['description']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from askme.models import Question, Answer, Like
from askme.forms import QuestionForm, AnswerForm, LikeForm


@login_required
def home(request):
    questions_detail = []
    questions = Question.objects.all().order_by('-created_at')
    for idx, question in enumerate(questions):
        q_details = {"id": question.id, "title": question.title, "description": question.description, "posted_by": question.posted_by.username, "rank": idx+1}

        answer_list = []
        answers = Answer.objects.filter(question=question).order_by("-created_at")
        for answer in answers:
            likes = Like.objects.filter(answer=answer).count()
            aleady_liked = Like.objects.filter(answer=answer, liked_by=request.user).exists()
            answer_list.append({"id": answer.id, "description": answer.description, "answerd_by": answer.answerd_by, "likes": likes, "show_like": not aleady_liked })
        q_details["answers"] = answer_list
        questions_detail.append(q_details)
    return render(request, 'home.html', {'questions': questions_detail})


@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.posted_by = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})


@login_required
def make_answer(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.answerd_by = request.user
            answer.question = question
            answer.save()
            return redirect('home')
    else:
        form = AnswerForm()
    return render(request, 'make_answer.html', {'form': form, 'question_id': question_id})


@login_required
def hit_like(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    if request.method == 'POST':
        Like.objects.get_or_create(liked_by=request.user, answer=answer)
        return redirect('home')
    return render(request, 'like_button.html', {'answer_id': answer_id})

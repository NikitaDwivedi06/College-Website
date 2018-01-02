from django.shortcuts import render
from .models import Question,Answer,Comments
from django.shortcuts import render, redirect
from media import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from student.models import Student
# Create your views here.



def post_list(request):
    posts = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    answers = Answer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    comments = Comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'answers': answers, 'comments': comments})

def post_question(request):
    return render(request, 'blog/post_question.html')


def extract_question(request):
    user = User.objects.get(username=request.POST.get('input-name'))
    ques=Question()
    ques.questioner=user
    ques.title=request.POST.get('input-subject')
    ques.text=request.POST.get('input-message')
    ques.created_date=timezone.now()
    ques.published_date=timezone.now()
    ques.save()
    posts = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    answers = Answer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    comments = Comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return HttpResponseRedirect("/blog")

def post_answer(request,que):
    return render(request, 'blog/post_answer.html',{'que':que})


def extract_answer(request):
    user = User.objects.get(username=request.POST.get('input-name'))
    questioner=Question.objects.get(id=request.POST.get('queno'))
    ans=Answer()
    ans.question=questioner
    ans.answerer=user
    ans.text=request.POST.get('input-message')
    ans.title=request.POST.get('input-subject')
    ans.created_date=timezone.now()
    ans.published_date=timezone.now()
    if (request.FILES.get("fileupload")):
        ans.photo = request.FILES.get("fileupload")
    ans.save();
    posts = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    answers = Answer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    comments = Comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return HttpResponseRedirect("/blog")

def post_comment(request,que,ans):
    return render(request, 'blog/post_comment.html',{'que':que,'ans':ans})

def extract_comment(request):
    user = User.objects.get(username=request.POST.get('input-name'))
    answerer = Answer.objects.get(id=request.POST.get('ansno'))
    questioner = Question.objects.get(id=request.POST.get('queno'))
    comment=Comments()
    comment.commenter = user
    comment.answer=answerer
    comment.question = questioner
    comment.text=request.POST['input-message']
    comment.title=request.POST['input-subject']
    comment.created_date=timezone.now()
    comment.published_date=timezone.now()
    comment.save()
    posts = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    answers = Answer.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    comments = Comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return HttpResponseRedirect("/blog")


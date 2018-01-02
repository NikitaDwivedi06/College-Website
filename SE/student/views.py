from bs4 import BeautifulSoup
import subprocess, urllib.request, html.parser
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView     #form for editing an object
from django.core.urlresolvers import reverse_lazy
from .models import Faculty, Language, Student, Assignment, Course, Question, Answer, Comments
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from media import *
import time
import glob
import zipfile
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
import difflib




def DisplayView(request):
    template_name = 'student/display.html'
    subject = str(request.POST.get("subject"))
    number = str(request.POST.get("number"))
    language = str(request.POST.get("lang"))
    dir = "no"             #indicates if asgns are submitted as directories
    moss = "media/moss.pl"
    file_list = []
    file_list.append("perl")
    file_list.append(moss)
    file_list.append("-l")
    file_list.append(language)
    file=""

    directory = "media/"+subject+"/"+number+"/*."+language

    if(dir=="no"):
        for filename in glob.iglob(directory):
            file_list.append(filename)



    if(dir=="yes"):                                        #NOTE: In this case, supply unzipped FOLDERS to MOSS
       directory_zipped = "/media/"+subject+"/"+number+"/*.zip"
       for zipped_file in directory_zipped:
           with zipfile.ZipFile(zipped_file,"r") as zip_ref:
               target = zip_ref.filename.spilt(".")[0]   #to split into filename and file extension
               zip_ref.extractall(target)
       file_list.append("-d")           #indicates that files supplied to MOSS are directories


    if(language=="txt"):     #do stuff with difflib








     p = subprocess.Popen(file_list, stdout = subprocess.PIPE)
     out, err = p.communicate()

     abc = out.decode('utf-8')
     file = abc.split("response.")[1]


    return render(request, template_name,{'link': file})


def show_loginform(request):
    return render(request, 'student/login.html')

def getcheckform(request):
    return render(request,'student/check-assgn.html')

def login(request):
   username = request.POST.get("user")
   password = request.POST.get("pass")

   student = Student()
   student = Student.objects.get(name=username)
   if(student.password==password):
       return render(request, 'student/loggedin.html',{'student':student})
   else:
       return render(request, 'student/login1.html')



def AssignmentAdd(request):
    student_name = request.POST.get("student-name")
    course_name = request.POST.get("course-name")
    language = Language.objects.all()
    return render(request,'student/add-assgn.html',{'sid':student_name, 'ccode':course_name, 'lang':language})

def SaveAssgn(request):
    course = request.POST.get("subject")
    author = request.POST.get("author")
    lang = request.POST.get("lang")
    num = request.POST.get("number")
    title = request.POST.get("title")
    files = request.FILES["file"]
    assg1 = Assignment()
    student = Student.objects.get(sid=author)
    assg1.author=student
    courseobj = Course()
    courseobj = Course.objects.get(code=course)
    assg1.subject = courseobj
    langs = Language.objects.get(name=lang)
    assg1.language=langs
    assg1.number=num
    assg1.title=title
    assg1.file = files
    assg1.save()
    return render(request,'student/loggedin.html',{'student':student})
    #return HttpResponseRedirect('/plagiarism/login')



from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, context_processors
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from .models import Courses, Course_details, Syllabus, Faculty, Assignment, Book, Paper
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from media import *
import time
import glob
import zipfile

import subprocess, urllib.request, html.parser

"""
def index(request):
    all_courses=Courses.objects.all() #retrieves objects from database replace this by objects.filter(professor__endswith='lname') get lname from session

    context = {                     #dictionary to store all course objects we need to pass this to template
        'all_courses' : all_courses,
    }
    return render(request,'courses/index.html',context)

def detail(request, course_id):
    try:
        course= Courses.objects.get(pk=course_id)
    except Courses.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request,'courses/detail.html',{'course':course})
"""

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/courses')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'courses/login.html', {})

def home(request):
    return render(request,'courses/home.html')

def process_login(request):
    username = request.POST.get("user")
    password = request.POST.get("pass")
    faculty = Faculty.objects.get(name=username)
    if(faculty.password==password):
       # return render(request,'index',{'faculty':faculty})
        #return render(request,'courses/index/')
        request.session['name']=username
        return HttpResponseRedirect('/courses')
    else:
       # return render(request,'courses/login.html')
        return render(request,'courses/home.html')


def syllabus(request,course_id):
    try:
        courses= Courses.objects.get(pk=course_id)
        syl = Syllabus.objects.filter(course=courses)
    except Courses.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request,'courses/syllabus.html',{'syl':syl})

def schedule(request,course_id):
    try:

        course= Courses.objects.get(pk=course_id)
        details=Course_details.objects.filter(course=course)
    except Courses.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request,'courses/schedule.html',{'details':details})

def books(request,course_id):
    try:
        course= Courses.objects.get(pk=course_id)
        books=Book.objects.filter(course=course)
    except Book.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request,'courses/book.html',{'books':books})

def assignment(request,course_id):
    try:
        course= Courses.objects.get(pk=course_id)
        asg = Assignment.objects.filter(course=course)
    except Assignment.DoesNotExist:
        raise Http404("Assignment does not exist")
    return render(request,'courses/assignment.html',{'asg':asg})

def contact(request,course_id):
    try:
        course= Courses.objects.get(pk=course_id)
        con = course.professor
    except Courses.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request,'courses/contact.html',{'con':con})

def paper(request, course_id):
        try:
            course= Courses.objects.get(pk=course_id)
            papers = Paper.objects.filter(course=course)
        except Paper.DoesNotExist:
            raise Http404("Paper does not exist")
        return render(request,'courses/paper.html',{'papers':papers})

def Index(request):
    try:
        if request.user.is_authenticated:
            n=request.user.get_username()
            #name=request.session['name']
        f=Faculty.objects.get(user=request.user)
        courses = Courses.objects.filter(professor=f)
    except Courses.DoesNotExist:
        raise Http404("Courses does not exist")
    return render(request,'courses/index.html',{'courses':courses})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/courses/home/')

def Detail(request, course_id):
    courses= Courses.objects.get(pk=course_id)
    return render(request,'courses/detail.html',{'courses':courses})
"""
class DetailView(generic.ListView):
    model = Courses
    template_name = 'courses/detail.html'
"""
#class DetailView(generic.ListView):
 #   model = Assignment
  #  template_name = 'courses/assignment.html'

class CoursesCreate(CreateView):
    model = Courses
    fields = ['professor', 'cname','cid','sem','year','session']
#default template suffix is_form so template is course_form

class CoursesUpdate(UpdateView):
    model = Courses
    fields = ['professor', 'cname','cid','sem','year','session']
#default template suffix is_form so template is course_form


class CoursesDelete(DeleteView):
    model = Courses
    success_url = reverse_lazy('index')

# default template suffix confirm_delete so template is course_confirm_delete
class Course_detailsCreate(CreateView):
    model =  Course_details
    #initial={'date':'mm/dd/yy'}
    fields = ['course','topic','notes','date']

class Course_detailsUpdate(UpdateView):
    model =  Course_details
    fields = ['course','topic','notes','date']

class Course_detailsDelete(DeleteView):
    model =  Course_details
    #success_url = reverse_lazy('schedule',kwargs={'course_id':object.course.pk})
    success_url = reverse_lazy('index')

class SyllabusCreate(CreateView):
    model = Syllabus
    fields=['course','topics']

class SyllabusUpdate(UpdateView):
    model = Syllabus
    fields=['course','topics']

class SyllabusDelete(DeleteView):
    model = Syllabus
    success_url = reverse_lazy('index')

class AssignmentCreate(CreateView):
    model = Assignment
    fields=['course','date','title','file']

class AssignmentUpdate(UpdateView):
    model = Assignment
    fields=['course','date','title','file']

class AssignmentDelete(DeleteView):
    model = Assignment
    success_url = reverse_lazy('index')

class BookCreate(CreateView):
    model = Book
    fields = ['course','name','link','pdf']

class BookUpdate(UpdateView):
    model = Book
    fields = ['course','name','link','pdf']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('index')

class PaperCreate(CreateView):
    model = Paper
    fields = ['course','exam','year','image']


class PaperUpdate(UpdateView):
    model = Paper
    fields = ['course','exam','year','image']

class PaperDelete(DeleteView):
    model = Paper
    success_url = reverse_lazy('index')



def evalasg(request, course_id):
    course = Courses.objects.get(pk=course_id)

    return render(request,'courses/evalasg.html',{'course':course, 'course_id':course_id})


def AsgPlg(request, course_id):
    template_name = 'courses/display.html'
    #take subject, number and lang from teacher
    subject = request.POST.get("subject")
    number = request.POST.get("number")
    language = "c"
    moss = "media/moss.pl"
    file_list = []
    file_list.append("perl")
    file_list.append(moss)
    file_list.append("-l")
    file_list.append(language)
    #remember to check the language of the assignment

    directory = "media/"+subject+"/"+number+"/*.c"

    for filename in glob.iglob(directory):
        file_list.append(filename)

    #else    NOTE: In this case, supply unzipped FOLDERS to MOSS
    '''
    directory_zipped = "/media/"+subject+"/"+number+"/*.zip"
    for zipped_file in directory_zipped:
           with zipfile.ZipFile(zipped_file,"r") as zip_ref:
               target = zip_ref.filename.spilt(".")[0]   #to split into filename and file extension
               zip_ref.extractall(target)
    '''




    p = subprocess.Popen(file_list, stdout = subprocess.PIPE)
    out, err = p.communicate()

    abc = out.decode('utf-8')
    file = abc.split("response.")[1]


    return render(request, template_name,{'link': file})
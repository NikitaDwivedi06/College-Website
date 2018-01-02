from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.
class Faculty(models.Model):
    user = models.OneToOneField(User)

    contact = models.IntegerField()
    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return self.user.username

class Courses(models.Model):
    professor = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    cname = models.CharField(max_length=75)
    cid =  models.CharField(max_length=10)
    sem =  models.IntegerField()
    year = models.IntegerField()
    session = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'course_id':self.pk})
    def __str__(self):
        return self.cid + '  ' + self.cname + '  ' + str(self.sem) + '  ' + str(self.year) + '  ' +self.session


class Course_details(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    #change this to pdf
    notes = models.FileField(blank=True, null=True)
    #date = models.DateTimeField(default=timezone.now)
    date = models.DateField()
    def get_absolute_url(self):
        return reverse('schedule',kwargs={'course_id':self.course.pk})
    def __str__(self):
        return self.topic


class Syllabus(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    topics = models.CharField(max_length=150)
    def get_absolute_url(self):
        return reverse('syllabus',kwargs={'course_id':self.course.pk})
    def __str__(self):
        return self.topics

class Assignment(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    file = models.FileField()
    def get_absolute_url(self):
        return reverse('assignment',kwargs={'course_id':self.course.pk})
   # def get_absolute_url(self):
    #    return reverse('asg')

class Book(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    pdf=models.FileField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse('books',kwargs={'course_id':self.course.pk})

class Paper(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    exam=models.CharField(max_length=20)
    year=models.IntegerField()
    image=models.FileField()
    def get_absolute_url(self):
        return reverse('paper',kwargs={'course_id':self.course.pk})


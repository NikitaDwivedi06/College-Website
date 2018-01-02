
from django.db import models
from django.utils import timezone


class Faculty(models.Model):
    fid = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20,default="PASS")

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=30)
    sem = models.CharField(max_length=1)   #eg: 5th sem
    year = models.CharField(max_length=1)  #eg: 1st year
    prof = models.ForeignKey(Faculty,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Student(models.Model):
    sid = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    rollno = models.CharField(default="BT00CSE000", max_length=10)
    year = models.CharField(max_length=4)     #year of graduation
    email = models.EmailField(max_length=30)
    courses = models.ManyToManyField(Course)  #a course has many students, and a student has multiple courses
    password = models.CharField(max_length=20,default="PASS")

    def __str__(self):
        return self.name

class Language(models.Model):                 #to store the acceptable programming languages
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

def Defined_Path(self, filename):
    return "%s/%s/%s" %(self.subject.name, self.number,self.author.rollno+"."+filename.split(".")[1])


class Assignment(models.Model):
    subject = models.ForeignKey(Course)
    number = models.CharField(max_length=2)             #asg number 1,2,3 etc
    title = models.CharField(max_length=20)
    language = models.ForeignKey(Language)     #the lang that the asg has been coded in
    author = models.ForeignKey(Student,default=None)
    file = models.FileField(upload_to=Defined_Path, verbose_name='File',blank=True,null=True)

    def __str__(self):
        return str(self.number)+". "+self.title+" ("+self.subject.name+")"


class Question(models.Model):
    questioner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
def Defined_Path(self,filename):
    return "%s/%s/" %('images',filename)

class Answer(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE,default=1)
    answerer=models.CharField(max_length=200);
    title = models.CharField(max_length=200)
    text=models.TextField()
    photo=models.FileField(upload_to=Defined_Path ,null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title


class Comments(models.Model):
    answer=models.ForeignKey('Answer',on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    commenter=models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title







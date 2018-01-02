from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    questioner = models.ForeignKey('auth.User',related_name="blog_users")
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
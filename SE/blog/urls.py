from django.conf.urls import url
from . import views


app_name="blog"

urlpatterns=[


    url(r'^$', views.post_list, name='post_list'),
    url(r'^post_question.html', views.post_question, name='post_question'),
    url(r'^extract_question',views.extract_question,name='extract_question'),
    url(r'^(?P<que>[0-9]+)/$',views.post_answer,name='post_answer'),
    url(r'^extract_answer',views.extract_answer,name='extract_answer'),
    url(r'^(?P<que>[0-9]+)/(?P<ans>[0-9]+)/$',views.post_comment,name='post_comment'),
    url(r'^extract_comment',views.extract_comment,name='extract_comment'),


]


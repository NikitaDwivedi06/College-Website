from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name="student"

urlpatterns=[
    #/student/
    url(r'^$', TemplateView.as_view(template_name='student/home.html'), name='home'),
    url(r'^loginform', views.show_loginform, name='loginform'),
    url(r'^login', views.login, name='login'),
    url(r'^add-assgn',views.AssignmentAdd, name='add-assgn'),
    url(r'^save-assgn', views.SaveAssgn, name='save-assgn'),
    url(r'^logout',TemplateView.as_view(template_name='student/logout.html'), name='logout'),

    #url(r'^home', TemplateView.as_view(template_name='student/home.html'), name='home'),




]

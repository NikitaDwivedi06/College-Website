
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



urlpatterns = [
 # courses/  homepage

 url(r'^home/$',views.home,name='home'),
 url(r'^home/login/$',TemplateView.as_view(template_name='courses/login.html'),name='login'),
 url(r'^facultyhome/$', views.user_login, name='facultyhome'),
 url(r'^$',views.Index,name='index'),
 url(r'^logout/$', views.user_logout, name='logout'),

 url(r'^(?P<course_id>[0-9]+)/evalasg/$',views.evalasg, name='evalasg'),
 url(r'^(?P<course_id>[0-9]+)/evalasg/asgplg/$', views.AsgPlg, name='asgplg'),

 url(r'^(?P<course_id>[0-9]+)/papers/$',views.paper,name='paper'),
 url(r'^(?P<course_id>[0-9]+)/papers/add/$',views.PaperCreate.as_view(),name='paper-add'),
 url(r'^(?P<course_id>[0-9]+)/papers/(?P<pk>[0-9]+)/update/$',views.PaperUpdate.as_view(),name='paper-update'),
 url(r'^(?P<course_id>[0-9]+)/papers/(?P<pk>[0-9]+)/delete/$',views.PaperDelete.as_view(),name='paper-del'),

 url(r'^(?P<course_id>[0-9]+)/schedule/$',views.schedule,name='schedule'),
 url(r'^(?P<course_id>[0-9]+)/schedule/add/$', views.Course_detailsCreate.as_view(),name='schedule-add'),
 url(r'^(?P<course_id>[0-9]+)/schedule/(?P<pk>[0-9]+)/update/$', views.Course_detailsUpdate.as_view(),name='schedule-update'),
 url(r'^(?P<course_id>[0-9]+)/schedule/(?P<pk>[0-9]+)/delete/$', views.Course_detailsDelete.as_view(),name='schedule-del'),

 url(r'^add/$',views.CoursesCreate.as_view(),name='courses-add'),
 url(r'^(?P<pk>[0-9]+)/update/$',views.CoursesUpdate.as_view(),name='courses-update'),
 url(r'^(?P<pk>[0-9]+)/delete/$',views.CoursesDelete.as_view(),name='courses-del'),
 #courses/3/
 #3 stored in course_id

 url(r'^(?P<course_id>[0-9]+)/syllabus/$',views.syllabus,name='syllabus'),
 url(r'^(?P<course_id>[0-9]+)/syllabus/add/$',views.SyllabusCreate.as_view(),name='syllabus-add'),
 url(r'^(?P<course_id>[0-9]+)/syllabus/(?P<pk>[0-9]+)/update/$',views.SyllabusUpdate.as_view(),name='syllabus-update'),
 url(r'^(?P<course_id>[0-9]+)/syllabus/(?P<pk>[0-9]+)/delete/$',views.SyllabusDelete.as_view(),name='syllabus-delete'),


 url(r'^(?P<course_id>[0-9]+)/books/$',views.books,name='books'),
 url(r'^(?P<course_id>[0-9]+)/books/add/$',views.BookCreate.as_view(),name='books-add'),
 url(r'^(?P<course_id>[0-9]+)/books/(?P<pk>[0-9]+)/update/$',views.BookUpdate.as_view(),name='books-update'),
 url(r'^(?P<course_id>[0-9]+)/books/(?P<pk>[0-9]+)/delete/$',views.BookDelete.as_view(),name='books-del'),

 url(r'^(?P<course_id>[0-9]+)/assignments/$',views.assignment,name='assignment'),
 url(r'^(?P<course_id>[0-9]+)/assignments/add/$',views. AssignmentCreate.as_view(),name='asg-add'),
 url(r'^(?P<course_id>[0-9]+)/assignments/(?P<pk>[0-9]+)/update/$',views. AssignmentUpdate.as_view(),name='asg-update'),
 url(r'^(?P<course_id>[0-9]+)/assignments/(?P<pk>[0-9]+)/delete/$',views. AssignmentDelete.as_view(),name='asg-delete'),

 url(r'^(?P<course_id>[0-9]+)/contact/$',views.contact,name='contact'),


 url(r'^(?P<course_id>[0-9]+)/$',views.Detail,name='detail'),




]
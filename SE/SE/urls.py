
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings             #for file uploading
from django.conf.urls.static import static   #for file uploading
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',include('home.urls') ,name='home'),
    url(r'^student/',include('student.urls',namespace='student')),
    url(r'^courses/', include('courses.urls')),
    url(r'^blog/', include('blog.urls',namespace='blog'))
]

if settings.DEBUG:       #in developer mode
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

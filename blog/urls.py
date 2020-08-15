from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#spliter

app_name = "blog"

urlpatterns = [
    path('',views.blogs,name='blog'),
    path('<int:blog_id>',views.detail,name="blog_id")
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'staff'

urlpatterns = [
    path('',views.staff,name='staff'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.logina,name='login'),
    path('logout/',views.logouta,name='logout'),
    path('create/',views.create,name='create'),
    path('change/',views.change,name='change'),
    path('change/<int:blog_id>',views.changeview,name='changeview'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
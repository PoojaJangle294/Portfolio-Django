from django.conf import settings
from django.urls import path, include
from .import views
urlpatterns=[
    path('',views.bhome,name='bhome'),
    path('<int:blog_id>/',views.detail,name='detail'),




]
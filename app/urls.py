from django.urls import path

from . import views

urlpatterns = [

   path('',views.index),
    path('out', views.out),
    path('work',views.work, name='work'),
    path('',views.out),

]

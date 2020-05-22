from django.contrib import admin
from django.urls import path
from mgr import students, teachers, managers

urlpatterns = [
     path('student/', students.dispatcher),
     path('teacher/', teachers.dispatcher),
     path('manager/', managers.dispatcher),
#     path('signin', sign_in_out.signin),
#     path('signout', sign_in_out.signout),
 ]
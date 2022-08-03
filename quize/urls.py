from django.urls import path
from .models import *
from .views import *


app_name = "quize"

urlpatterns = [

path('question/', create_questions.as_view(), name='TodoListApiView'),
path('answer/', create_answers.as_view(), name='TodoListApiView'),
path('relation/', relations.as_view(), name='TodoListApiView'),

]
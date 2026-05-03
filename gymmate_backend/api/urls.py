from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_trainer, name='login'),
    path('users/', views.get_all_users, name='users'),
    path('questions/', views.get_questions, name='questions'),
    path('answer/<str:question_id>/', views.answer_question, name='answer'),
    path('assign-workout/', views.assign_workout, name='assign_workout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('api-start/', views.start_quiz, name='start_quiz'),
    path('api-question/', views.get_question, name='get_question'),
    path('api-submit/', views.submit_answer, name='submit_answer'),
    path('api-results/', views.get_results, name='get_results'),
    path('start/', views.start_quiz_view, name='start_quiz_view'),
    path('question/', views.get_question_view, name='get_question_view'),
    path('results/', views.get_results_view, name='get_results_view'),
]
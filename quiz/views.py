import random
from django.http import JsonResponse
from .models import Question, UserSession
from django.shortcuts import render

def start_quiz(request):
    user_id = request.GET.get('user_id', 'default_user')
    session, created = UserSession.objects.get_or_create(user_id=user_id)
    session.total_questions = 0
    session.correct_answers = 0
    session.incorrect_answers = 0
    session.save()
    return JsonResponse({"message": "Quiz started:-", "user_id": user_id})

def get_question(request):
    question = random.choice(Question.objects.all())
    question_data = {
        "id": question.id,
        "question_text": question.question_text,
        "options": [question.option1, question.option2, question.option3, question.option4],
    }
    return JsonResponse(question_data)

def submit_answer(request):
    user_id = request.GET.get('user_id', 'default_user')
    question_id = request.GET.get('question_id')
    selected_option = int(request.GET.get('selected_option', 0))

    try:
        question = Question.objects.get(id=question_id)
        session = UserSession.objects.get(user_id=user_id)

        session.total_questions += 1
        if question.correct_option == selected_option:
            session.correct_answers += 1
            result = "Correct!"
        else:
            session.incorrect_answers += 1
            result = "Incorrect!"
        
        session.save()
        return JsonResponse({"result": result, "correct_option": question.correct_option})
    except Question.DoesNotExist:
        return JsonResponse({"error": "Invalid question ID"})
    except UserSession.DoesNotExist:
        return JsonResponse({"error": "Session not found"})

def get_results(request):
    user_id = request.GET.get('user_id', 'default_user')
    try:
        session = UserSession.objects.get(user_id=user_id)
        results = {
            "total_questions": session.total_questions,
            "correct_answers": session.correct_answers,
            "incorrect_answers": session.incorrect_answers,
        }
        return JsonResponse(results)
    except UserSession.DoesNotExist:
        return JsonResponse({"error": "Session not found."})

def start_quiz_view(request):
    return render(request, 'quiz/start.html')

def get_question_view(request):
    return render(request, 'quiz/question.html')

def get_results_view(request):
    return render(request, 'quiz/results.html')
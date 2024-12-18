import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizApp.settings')
django.setup()

from quiz.models import Question

csv_file_path = 'quiz.csv'

with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Question.objects.create(
            question_text=row['question_text'],
            option1=row['option1'],
            option2=row['option2'],
            option3=row['option3'],
            option4=row['option4'],
            correct_option=int(row['correct_option']),
        )

print("Questions imported successfully!")
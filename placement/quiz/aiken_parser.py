import os
import sys
import django
from .models import *

# Add your Django project directory to the sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
django.setup()


def parse_aiken_quiz(file_path):
    """
    Parses an Aiken quiz script and generates Django quiz objects.
    """
    with open(file_path, 'r') as f:
        quiz_lines = f.readlines()

    # Parse the quiz title
    title_line = quiz_lines.pop(0).strip()
    title = title_line.split(':')[1].strip()

    # Create the Quiz object
    quiz = Quiz.objects.create(title=title)

    # Parse the questions and answers
    question_text = ''
    correct_answer = None
    for line in quiz_lines:
        if line.startswith('A.'):
            # Parse the answer
            answer_text = line[2:].strip()
            is_correct = False
            if line.startswith('ANSWER:'):
                # This is the correct answer
                is_correct = True
                correct_answer = Answer.objects.create(text=answer_text)
            else:
                # This is an incorrect answer
                Answer.objects.create(text=answer_text, is_correct=False)

            # Create the answer for the current question
            Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

        elif line.startswith('ANSWER:'):
            # This is the correct answer
            answer_text = line[7:].strip()
            correct_answer = Answer.objects.create(text=answer_text)

        else:
            # Parse the question
            if question_text:
                # Create the previous question object
                question = Question.objects.create(quiz=quiz, text=question_text, correct_answer=correct_answer)
                question_text = ''
                correct_answer = None

            question_text += line.strip()

    # Create the last question object
    question = Question.objects.create(quiz=quiz, text=question_text, correct_answer=correct_answer)

    print(f'Successfully generated quiz: {quiz.title}')


if __name__ == '__main__':
    file_path = 'quiz1.txt'  # Change this to the file path of your Aiken quiz script
    parse_aiken_quiz(file_path)

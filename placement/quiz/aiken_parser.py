from .models import *


def parse_aiken_file(filename):
    # Open the Aiken file and read the contents
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Parse the Aiken file and create Quiz, Question, and Answer objects
    quiz_title = lines[0].strip()
    quiz = Quiz.objects.create(title=quiz_title)
    question_text = ''
    for line in lines[1:]:
        if line.startswith('A.'):
            answer_text = line[2:].strip()
            is_correct = answer_text.startswith('*')
            if is_correct:
                answer_text = answer_text[1:].strip()
            Answer.objects.create(text=answer_text, is_correct=is_correct, question=question)
        else:
            if question_text:
                question = Question.objects.create(text=question_text, quiz=quiz)
            question_text = line.strip()
    # Create the last question after the loop
    question = Question.objects.create(text=question_text, quiz=quiz)


if __name__ == '__main__':
    parse_aiken_file('quiz1.txt')

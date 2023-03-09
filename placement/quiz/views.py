from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from quiz.models import Quiz, Question, Answer


class IndexView(View):
    def get(self, request):
        quizzes = Quiz.objects.all()
        context = {'quizzes': quizzes}
        return render(request, 'quiz/index.html', context)


class QuizCreateView(View):
    def get(self, request):
        return render(request, 'quiz/quiz_create.html')

    def post(self, request):
        # Parse the Aiken file from the request
        aiken_text = request.POST.get('aiken_text')
        quiz_title, questions = aiken_parser.parse(aiken_text)

        # Create the Quiz object and save it to the database
        quiz = Quiz.objects.create(title=quiz_title)

        # Create the Question and Answer objects and save them to the database
        for question_text, answer_text, options_text in questions:
            question = Question.objects.create(text=question_text, quiz=quiz)
            for option_text in options_text:
                is_correct = option_text == answer_text
                Answer.objects.create(text=option_text, question=question, is_correct=is_correct)

        messages.success(request, 'Quiz created successfully.')
        return redirect('quiz:index')


class QuizDetailView(View):
    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = quiz.question_set.all()
        context = {'quiz': quiz, 'questions': questions}
        return render(request, 'quiz/quiz_detail.html', context)

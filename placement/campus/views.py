from hashlib import sha256

import stripe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.sites import requests
from django.views import View
from .forms import *

from django.template import loader

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import EmailMultiAlternatives

from django.conf import settings
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import RegisterForm, LoginForm
from .decorators import user_login_required
import random
from placement.settings import EMAIL_HOST_USER

from notifications.signals import notify

from .aiken import Aiken

"""imports for Machine Learning Algorithms"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# user model
User = get_user_model()


# Create your views here.

# sender = User.objects.get(username=request.user)
# recipient = User.objects.get(id=user_id)
# message = "This is an simple message"
# notify.send(actor=sender, recipient=recipient, verb='Message',
#             description=message)


def ajax_generate_code(request):
    print(request.GET)
    for x in request.GET:
        if x != '_':
            email = x
            # Generate Code and save it in a session
            request.session['code'] = random.randint(111111, 999999)
            # Send email Functionality
            text_content = "Your Email Verification Code for Placement-Cell Registration is " + str(
                request.session['code'])
            msg = EmailMultiAlternatives('Verify Email', text_content, EMAIL_HOST_USER, [email])
            msg.send()
    return HttpResponse("success")


# def activateEmail(request, user, to_email):
#     mail_subject = "Activate your user account."
#     messages = render_to_string()


def register(request):
    form = RegisterForm()
    # is_private = request.POST.get('is_private', False)
    success = None
    if request.method == 'POST':
        if StudentReg.objects.filter(admino=request.POST['admino']).exists():
            error = "This Admission number is already taken"
            return render(request, 'campus/register.html', {'form': form, 'error': error})

        if StudentReg.objects.filter(email=request.POST['email']).exists():
            error = "This email is already taken"
            return render(request, 'campus/register.html', {'form': form, 'error': error})

        ## Check Verification Code
        if (not 'code' in request.POST) or (not 'code' in request.session) or (
                not request.POST['code'] == str(request.session['code'])):
            error = "Invalid Verification Code"
            return render(request, 'campus/register.html', {'form': form, 'error': error})
            ## Safe to go
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New User Created Successfully, You may go back and try to login !"
    return render(request, 'campus/register.html', {'form': form, 'success': success})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if StudentReg.objects.filter(email=email, password=password).exists():
            user = StudentReg.objects.filter(email=email)
            for std in user:
                email = std.email
                id = std.admino
                print(email, id)
                request.session['email'] = std.email
                """This is a session variable and will remain existing as long as you don't delete this manually or 
                clear your browser cache """
                request.session['admino'] = id
                return redirect('campus:student')
        error = "Credentials not match! Try again"
        return render(request, 'campus/login.html', {'form': form, 'error': error})
    else:
        return render(request, 'campus/login.html', {'form': form})


def update_password(request):
    return render(request, 'campus/update_password.html')


def password_changed(request):
    form = PasswordChangeForm()
    email = request.session['email']
    uemail = request.POST.get['email']
    if request.method == 'POST':
        if form.is_valid():
            if email == uemail:
                password = request.POST.get['password']
                print(password)
                return render(request, 'campus/adminDashboard.html')
            else:
                return HttpResponse(
                    "<script>alert('oops! Registered email and entered email does not match! Try again');window.location='/';</script>")
        else:
            messages.error(request, 'Please correct the error below.')


def tpoLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Tpo.objects.filter(tpoMail=email, tpoPassword=password).exists():
            user = Tpo.objects.get(tpoMail=email)
            request.session['tpoMail'] = user.tpoMail
            # This is a session variable and will remain existing as long as you don't delete this manually or clear your browser cache
            return redirect('adminDash')
        return render(request, 'campus/adminLogin.html', {'form': form})
    else:
        return render(request, 'campus/adminLogin.html', {'form': form})


def get_admin(request):
    return Tpo.objects.get(tpoMail=request.session['tpoMail'])


@login_required(login_url='tpoLogin')
def adminDash(request):
    user = get_admin(request)
    return render(request, 'campus/adminDashboard.html', {'user': user})


def tpoLogout(request):
    if 'email' in request.session:
        del request.session['email']  # delete user session
    return redirect('campus:tpo')


def get_user(request):
    # request.session['admino']=13312
    return StudentReg.objects.get(email=request.session['email'])


def home(request):
    if 'email' in request.session:
        user = get_user(request)
        return render(request, 'campus/studentDashboard.html', {'user': user})
    else:
        return render(request, 'campus/login.html')


@user_login_required
def studentDash(request):
    email = request.session['email']
    user = get_user(request)
    myData = StudentReg.objects.filter(admino=user.admino)
    quiz_result = QuizResult.objects.filter(email=email)
    aiken_result = Aiken_Result.objects.filter(email=email)
    # print(myData)
    context = {
        'user': user,
        'myData': myData,
        'quiz_result': quiz_result,
        'aiken_result': aiken_result,
    }
    return render(request, 'campus/studentDashboard.html', context)


def logout(request):
    if 'email' in request.session:
        request.session.clear()  # delete user session
    return redirect('/')


# def logout(request):
#     try:
#         del request.session['email']
#     except KeyError:
#         pass
#     return render(request, "campus/login.html")


def tpo(request):
    return render(request, 'campus/adminLogin.html')


# def studentDash(request):
#     return render(request, 'campus/studentDashboard.html')

# @login_required(login_url='login')
def updateStudentDetails(request):
    email = request.session['email']
    if Payment.objects.filter(email=email).exists():
        form = MCAStudentDetails()
        # is_private = request.POST.get('is_private', False)
        success = None
        if request.method == 'POST':
            form = MCAStudentDetails(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.admino = email
                data.save()
            success = "Updated Successfully !"
        return render(request, 'campus/student_details.html', {'form': form, 'success': success})
    else:
        return render(request, 'campus/payments.html', )


@login_required(login_url='login')
def password_change(request):
    user = request.user
    form = SetPasswordForm(user)
    return render(request, 'password_reset_form.html', {'form': form})


@user_login_required
def viewDrive(request):
    email = request.session['email']
    if Payment.objects.filter(email=email).exists():
        user = get_user(request)
        viewDrive = Drives.objects.all()
        myData = StudentReg.objects.get(email=user.email)
        return render(request, 'campus/viewDrive.html', {'myData': myData, 'viewDrive': viewDrive})
    else:
        return render(request, 'campus/payments.html', )


@user_login_required
def applyDrive(request):
    return HttpResponse("<script>alert('Congrats! Applied Successfully');window.location='/';</script>")
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     full_name = request.POST['full_name']
    #     print(email)
    #     if ApplyDrive.objects.filter(email=email, full_name=full_name).exists():
    #         return HttpResponse("<script>alert('Already Applied!');window.location='/viewDrive';</script>")
    #     else:
    #         drive = ApplyDrive(email=email, full_name=full_name, job_name='TCS')
    #         drive.save()
    #         return HttpResponse("<script>alert('Applied Successful!');window.location='/viewDrive';</script>")
    # else:
    #     redirect('applyDrive')


@user_login_required
def registerDrive(request):
    viewDrive = Drives.objects.all()
    return render(request, 'campus/registerDrive.html')


@user_login_required
def payment(request):
    email = request.session['email']
    user = get_user(request)
    myData = StudentReg.objects.filter(admino=user.admino)
    if Payment.objects.filter(email=email).exists():
        info = Payment.objects.filter(email=email).values('payment_on').get()['payment_on']
        context = {
            'info': info,
            'myData': myData,
        }
        print(info)
        return render(request, 'campus/payment_done.html', context)
        # return HttpResponse("<script>alert('Already Paid!');window.location='/';</script>")
    else:
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1MfyQ0SIBKZt2GrFUxYh2TYT',
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('campus:thanks')) + '?session_id = {CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('campus:home')),
        )
        context = {
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
    return render(request, 'campus/payments.html', context)


@user_login_required
def thanks(request):
    email = request.session['email']
    status = 'paid'
    print(email)
    if not Payment.objects.filter(email=email).exists():
        r = Payment(email=email, status=status)
        r.save()
        print(r)
    else:
        return HttpResponse("<script>alert('You just Paid your fee!');window.location='/student';</script>")

    return render(request, 'campus/studentDashboard.html')


def quiz(request):
    email = request.session['email']
    if Payment.objects.filter(email=email).exists():
        if request.method == 'POST':
            print(request.POST)
            questions = QuesModel.objects.all()
            time = request.POST.get('timer')
            score = 0
            wrong = 0
            correct = 0
            total = 0
            cgpa = 6.9
            for q in questions:
                total += 1
                print(request.POST.get(q.question))
                print('correct answer:' + q.ans)
                print()
                if q.ans == request.POST.get(q.question):
                    score += 1
                    correct += 1
                else:
                    wrong += 1
            percent = (score / total) * 100
            analysis = performance_predict(correct, total, cgpa, time)
            performance = round(analysis, 2)
            if percent < 30:
                performance = 'You must have to improve yourself'
            elif percent <= 60:
                performance = 'Above average performance. But have to improve'
            elif 60 < percent <= 85:
                performance = 'Awsome performance!'
            else:
                performance = 'Mind blowing! Congrats Champ'
            print('performance:', performance)
            context = {
                'score': score,
                'time': time,
                'correct': correct,
                'wrong': wrong,
                'percent': percent,
                'total': total,
                'performance': performance,
            }

            r = QuizResult(email=email, score=score, time=time + ' sec', correct=correct,
                           wrong=wrong, percent=percent, total=total)
            print('email:', r.email, '\nscore:', r.score, '\ntime:', r.time, '\ncorrect:', r.correct, '\nwrong:',
                  r.wrong, '\npercentage:', r.percent, '\ntotal:', r.total)
            r.save()

            return render(request, 'campus/result.html', context)
        else:
            questions = QuesModel.objects.all()
            print(questions)
            if not questions:
                return HttpResponse(
                    "<script>alert('No Quiz for the practice mode. Try again later!..'); window.location='quiz_mode'; </script>"
                )
            else:
                context = {
                    'questions': questions,
                }
                return render(request, 'campus/quizpage.html', context)
    else:
        return render(request, 'campus/payments.html', )


def quiz_mode(request):
    email = request.session['email']
    user = get_user(request)
    myData = StudentReg.objects.filter(admino=user.admino)
    context = {
        'user': user,
        'myData': myData,
    }
    if Payment.objects.filter(email=email).exists():
        return render(request, 'campus/quiz_mode.html', context)
    else:
        return render(request, 'campus/payments.html', )


def quiz_list(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes': quizzes,
    }
    print(quizzes)
    # print(aiken_quiz)

    if not quizzes:
        return HttpResponse(
            "<script>alert('Nothing is Scheduled by the TPO!'); window.location='quiz_mode'; </script>"
        )
    else:
        return render(request, 'campus/quiz_list.html', context)


def quiz_detail(request, id):
    # question = AikenQuizFormat.objects.filter(id=id)
    attempts = AikenFile.objects.filter(id=id).values('attempts').get()['attempts']
    print('attempts: ',attempts)

    # attempt_counter = Aiken_Result.objects.filter(id=id).values('counter').get()['counter']
    # print(attempt_counter)

    # if attempt_counter < attempts:
    data = AikenFile.objects.get(id=id)
    print(data)
    print(id)

    times = AikenFile.objects.filter(id=id).values('time').get()['time']
    print(times)
    quiz = Quiz.objects.get(id=id)
    questions = quiz.question_set.all()

    print('questions : \n', questions)
    print('Quiz:', quiz)

    context = {
        'quiz': quiz,
        'questions': questions,
        'times': times,
    }
    return render(request, 'campus/quiz_details.html', context)
    # else:
    #     return HttpResponse(
    #         "<script>alert('You have already completed all of your attempts!'); window.location='/quiz_list'; </script>"
    #     )


def submit_quiz(request, id):
    email = request.session['email']
    quiz = get_object_or_404(Quiz, pk=id)
    quiz_name=AikenFile.objects.filter(id=id).values('id').get()['id']
    print('quiz_name: ', quiz_name)
    counter = AikenFile.objects.filter(id=id).values('attempts').get()['attempts']
    print('counter: ', counter)
    print('Quiz ID: ', quiz)
    if request.method == 'POST':
        quiz_id = id
        score = 0
        quiz_name = quiz
        time = request.POST.get('total_sec')
        correct = 0
        wrong = 0
        percent = 0
        total = 0

        for question in quiz.question_set.all():
            answer_id = request.POST.get(f'question_{question.id}')
            print('Answer ID :', answer_id)
            total += 1
            if answer_id:
                answer = get_object_or_404(Answer, pk=answer_id)
                print('Answer :', answer)
                if answer.is_correct:
                    correct += 1
                    print('Correct Answer :', answer.is_correct)
                    score += 1
                    print(score)
                else:
                    wrong += 1
                    print('Wrong Answer')
        percent = (score / total) * 100
        print('Total Mark : ', score)
        counter += 1
        print('counter: ', counter)
        r = Aiken_Result(quiz_id=quiz_name, email=email, score=score, quiz_name=quiz_name, time=time, correct=correct, wrong=wrong,
                         percent=percent, total=total, counter=counter)
        r.save()
        print(r)
        context = {
            'quiz_id': id,
            'quiz': quiz,
            'email': email,
            'score': score,
            'quiz_name': quiz_name,
            'time': time,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'counter': counter
        }
        return render(request, 'campus/quiz_results.html', context)
    return render(request, 'campus/quiz_list.html', {'quiz': quiz})


def performance_predict(correct, total, cgpa, time):
    print(correct, total, cgpa, time)
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv('static/csv/Student.csv')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop('output', axis=1), df['output'], test_size=0.2,
                                                        random_state=0)

    # Create a Linear Regression model and fit it to the training data
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = regressor.predict(X_test)

    # Evaluate the performance of the model
    from sklearn.metrics import mean_squared_error, r2_score
    print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
    print('Coefficient of determination (R^2): %.2f' % r2_score(y_test, y_pred))
    print('Accuracy : %.2f' % (r2_score(y_test, y_pred) * 100))

    return r2_score(y_test, y_pred) * 100

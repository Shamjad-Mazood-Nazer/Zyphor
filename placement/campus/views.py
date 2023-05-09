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
from datetime import *

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

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from django.template.loader import get_template
from django.template import Context

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


def login_view(request):
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
    email = request.session['email']
    user = StudentReg.objects.get(email=email)
    context = {
        'user': user,
    }
    return render(request, 'campus/update_password.html', context)


def password_changed(request):
    # form = PasswordChangeForm()
    email = request.session['email']
    quiz_result = QuizResult.objects.filter(email=email)
    aiken_result = Aiken_Result.objects.filter(email=email)
    print(email)
    old_password = StudentReg.objects.filter(email=email).values('password').get()['password']
    print(old_password)
    current_password = request.POST['current-password']
    password = request.POST['new-password']
    print(current_password)
    print(password)
    if request.method == 'POST':
        if current_password == old_password:
            r = StudentReg.objects.get(email=email)
            r.password = password
            r.save()
            print(r)
            user = StudentReg.objects.get(email=email)
            print('Admino: ', user.admino)
            message = "Your password is now updated successfully!"
            context = {
                'quiz_result': quiz_result,
                'aiken_result': aiken_result,
                'message': message,
                'user': user,
            }
            return render(request, 'campus/update_password_success.html', context)
        else:
            return HttpResponse(
                "<script>alert('Current password is incorrect! Try again');window.location='/';</script>")
    else:
        print('not post')
        messages.error(request, 'Please correct the error below.')
        return render(request, 'campus/studentDashboard.html', {})


def change_profile_picture(request):
    return render(request, 'campus/student_profile.html')


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
    images = Company_Image.objects.all()
    if 'email' in request.session:
        email = request.session['email']
        user = get_user(request)
        print('ID: ', user.id)
        quiz_result = QuizResult.objects.filter(email=email)
        aiken_result = Aiken_Result.objects.filter(email=email)
        context = {
            'user': user,
            'quiz_result': quiz_result,
            'aiken_result': aiken_result,
        }
        return render(request, 'campus/studentDashboard.html', context)
    else:
        return render(request, 'campus/index.html', {'images': images})


@user_login_required
def studentDash(request):
    email = request.session['email']
    user = get_user(request)
    myData = StudentReg.objects.filter(admino=user.admino)
    quiz_result = QuizResult.objects.filter(email=email)
    aiken_result = Aiken_Result.objects.filter(email=email)
    total_score = 0
    total_questions = 0
    for result in aiken_result:
        total_score = total_score + int(result.score)
        total_questions = total_questions + int(result.total)
    if total_questions != 0:
        average = (total_score / total_questions) * 100
        average_score = round(average, 2)
        print('correct: ', total_score, '\nquestion: ', total_questions, '\naverage: ', average_score)
    else:
        average_score = 0
        print('No questions answered yet.')
    # quiz_results = Aiken_Result.objects.filter(email=request.user.email).values_list('score', flat=True)
    # print(aiken_result, '\nquiz_results: ', quiz_results)
    # print(myData)
    context = {
        'user': user,
        'myData': myData,
        'quiz_result': quiz_result,
        'aiken_result': aiken_result,
        'total_score': total_score,
        'total_questions': total_questions,
        'average_score': average_score,
        # 'quiz_results': quiz_results,
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


def student_profile(request):
    email = request.session['email']
    user = get_user(request)
    myData = StudentReg.objects.get(email=user.email)
    id = myData.id
    details = MCAStudentDetails.objects.get(user=id)

    context = {
        'user': myData,
        'details': details,
    }
    return render(request, 'campus/student_profile.html', context)


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


def update_profile(request):
    email = request.session['email']
    user = get_user(request)
    print(user)
    myData = StudentReg.objects.filter(admino=user)
    quiz_result = QuizResult.objects.filter(email=email)
    aiken_result = Aiken_Result.objects.filter(email=email)
    phone1 = request.POST['phone1']
    phone2 = request.POST['phone2']
    address = request.POST['address']
    pincode = request.POST['pincode']
    district = request.POST['district']
    print(phone1, phone2, address, pincode, district)
    # id = myData
    # print(id)
    if request.method == 'POST':
        r = MCAStudentDetails.objects.get(user=user)
        print(r.mobileNoIndian)
        r.mobileNoIndian = phone1
        print(r.mobileNoIndian)
        r.alternativeNo = phone2
        r.fullAddress = address
        r.pincode = pincode
        print(r.district)
        r.district = district
        print(r.district)
        r.save()
        print(r)
        context = {
            'user': user,
            'myData': myData,
            'quiz_result': quiz_result,
            'aiken_result': aiken_result,
        }
        return HttpResponse(
            "<script>alert('Details updated!'); window.location='studentDash'; </script>"
        )
    return render(request, 'campus/student_profile.html')


@login_required(login_url='login')
def password_change(request):
    user = request.user
    form = SetPasswordForm(user)
    return render(request, 'password_reset_form.html', {'form': form})


@user_login_required
def viewDrive(request):
    email = request.session['email']
    if Payment.objects.filter(email=email).exists():
        display_drives = []
        end_drives = []
        user = get_user(request)
        viewDrive = Drives.objects.all().order_by('-last_date')
        myData = StudentReg.objects.get(email=user.email)
        print(myData.id, myData.first_name)
        id = myData.id
        try:
            stddetails = MCAStudentDetails.objects.get(user=id)
        except MCAStudentDetails.DoesNotExist:
            # Handle the case where no MCAStudentDetails record is found
            stddetails = None
        print(stddetails)
        if stddetails is None:
            return HttpResponse(
                "<script>alert('Your details were not uploaded! Please do that first.'); "
                "window.location='updateStudentDetails'; </script>"
            )
        else:
            print('DOB: ', stddetails.DoB)
            print('Foreign Obj: ', stddetails)
            print('Student CGPA: ', stddetails.ugCgpa)
            # return render(request, 'campus/viewDrive.html', {'user': myData, 'viewDrive': viewDrive})

            for drive in viewDrive:
                print('Drive ID: ', drive.id)
                print(stddetails.ugCgpa, '>=', drive.cgpa)
                print(stddetails.ugPer, '>=', drive.ug_percentage)
                print(stddetails.mcaPer, '>=', drive.pg_percentage)
                print(stddetails.activeArrears, '>=', drive.backlog)

                if float(stddetails.ugCgpa) >= drive.cgpa and float(stddetails.ugPer) >= drive.ug_percentage and float(
                        stddetails.mcaPer) >= drive.pg_percentage and int(stddetails.activeArrears) <= drive.backlog:
                    if datetime.today().date() <= drive.last_date:
                        display_drives.append(drive.id)
                        print('Drives Count: ', display_drives)
                    else:
                        end_drives.append(drive.id)
                        print('End Drives Count: ', end_drives)
                else:
                    print('Total Count: ', display_drives + end_drives)

            if display_drives is None:
                error = "Sorry, Your profile was not met the Academic profile that recruiters needs. Kindly " \
                        "please wait for your turn"
                context = {
                    'user': myData,
                    'error': error
                }
                return render(request, 'campus/viewDrive.html', context)
            else:
                context = {
                    'user': myData,
                    'viewDrive': viewDrive,
                    'display_drives': display_drives,
                    'end_drives': end_drives,
                }
                # print(display_drives.company_name)
                return render(request, 'campus/viewDrive.html', context)
            # return render(request, 'campus/viewDrive.html', {'user': myData, 'viewDrive': viewDrive})
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
def register_drive(request, id):
    email = request.session['email']
    user = get_user(request)
    drives = Drives.objects.all()
    last_date = Drives.objects.filter(id=id).values('last_date').get()['last_date']
    drive_id = Drives.objects.get(id=id)
    # applied_date = ApplyDrive.objects.filter(drive_name=id).values('applied_on').get()['applied_on']
    myData = StudentReg.objects.get(email=user.email)
    print('Drives: ', drives, '\nlast_date: ', last_date, '\ndrive_id: ', drive_id, '\nmyData: ', myData)
    print('Today: ', datetime.today().date(), '\n', )
    if datetime.today().date() <= last_date:
        print('Test on IF')
        if ApplyDrive.objects.filter(drive_name=drive_id, user=myData).exists():
            print('working on IF')
            applied_on = ApplyDrive.objects.get(drive_name=drive_id, user=myData).applied_on
            applied_on_str = applied_on.strftime('%d-%m-%Y')
            return HttpResponse(
                "<script>alert('Already applied on {}!..'); window.location='/viewDrive'; </script>".format(
                    applied_on_str)
            )
            # return HttpResponse(
            #     "<script>alert('Already applied on {}!..'); window.location='/viewDrive'; </script>".format(
            #         drive_id.last_date.strftime('%d-%m-%Y'))
            # )
        else:
            print('testing on else')
            r = ApplyDrive(drive_name=drive_id, user=myData, status=True)
            print('drive_name: ', drive_id, 'user: ', myData.id, 'status: ', True)
            r.save()

            context = {
                'user': myData,
                'drives': drives,
            }
            return HttpResponse("<script>alert('Successfully Applied to {} !..'); window.location='/viewDrive'; "
                                "</script>".format(drive_id)
                                )
    else:
        print('testing outer else')
        return HttpResponse("<script>alert('Currently we are not accepting any request for this Drive from {}!..'); "
                            "window.location='/viewDrive';</script>".format(last_date.strftime('%d-%m-%Y'))
                            )


@user_login_required
def payment(request):
    email = request.session['email']
    # user = get_user(request)
    # myData = StudentReg.objects.filter(admino=user.admino)
    user = StudentReg.objects.get(email=email)
    if Payment.objects.filter(email=email).exists():
        info = Payment.objects.filter(email=email).values('payment_on').get()['payment_on']
        transaction_id = Payment.objects.filter(email=email).values('transaction_id').get()['transaction_id']
        context = {
            'info': info,
            'user': user,
            'transaction_id': transaction_id,
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
            success_url=request.build_absolute_uri(reverse('campus:thanks')).replace('%20', '') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('campus:home')),
        )
        context = {
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        }
        print(context)
    return render(request, 'campus/payments.html', context)


# @user_login_required
def thanks(request):
    session_id = request.GET.get('session_id')  # Retrieve the session ID from the URL parameters
    print(session_id)  # Debugging statement to check the value of session_id

    # Retrieve the session details from Stripe using the session ID
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        print(session)  # Debugging statement to check the session details

        if session.payment_intent is not None:
            transaction_id = session.payment_intent
            # Save the transaction ID to your database or perform any necessary actions
            email = request.session['email']
            status = 'paid'
            if not Payment.objects.filter(email=email).exists():
                r = Payment(email=email, status=status, transaction_id=transaction_id)
                r.save()
                print(r)
            else:
                return HttpResponse("<script>alert('You just Paid your fee!');window.location='/payment';</script>")

            return render(request, 'campus/thanks.html')
        else:
            return redirect('campus:payment')  # Redirect to an error page

    except stripe.error.InvalidRequestError as e:
        print(e)  # Debugging statement to print the exception details
        return redirect('campus:payment')  # Redirect to an error page


@user_login_required
def generate_receipt(request):
    # Get the payment information from the request or database
    email = request.session['email']
    first_name = StudentReg.objects.filter(email=email).values('first_name').get()['first_name']
    last_name = StudentReg.objects.filter(email=email).values('last_name').get()['last_name']
    payment_amount = 5000
    fetch_date = Payment.objects.filter(email=email).values('payment_on').get()['payment_on']
    transaction_id = Payment.objects.filter(email=email).values('transaction_id').get()['transaction_id']
    payment_date = fetch_date.date()
    payment_method = 'Credit card'
    customer_name = first_name + ' ' + last_name

    # Create a PDF document using ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="payment_receipt.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()

    # Define the elements for the PDF document
    elements = []
    elements.append(Paragraph('Zyphor - Payment Receipt', styles['Heading1']))
    elements.append(Spacer(1, 0.2 * inch))

    # Add the payment information to the PDF document
    table_data = [
        ['Bill'],
        ['Recipient Name:', customer_name],
        ['Payment Amount:', payment_amount],
        ['Stripe Transaction ID:', transaction_id],
        ['Payment Date:', payment_date],
        ['Payment Method:', payment_method],
    ]
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    elements.append(Table(table_data, style=table_style))

    # Add a “Thank You” message to the PDF document
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph('Thank You for your payment!', styles['Normal']))

    # Build the PDF document from the elements
    doc.build(elements)

    return response


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
                    "<script>alert('No Quiz for the practice mode. Try again later!..'); window.location='quiz_mode'; "
                    "</script>"
                )
            else:
                context = {
                    'questions': questions,
                }
                return render(request, 'campus/quizpage.html', context)
    else:
        return render(request, 'campus/payments.html', )


@user_login_required
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


@user_login_required
def quiz_list(request):
    email = request.session['email']
    quizzes = Quiz.objects.all()
    quiz_details = AikenFile.objects.all()
    user = StudentReg.objects.get(email=email)
    context = {
        'quizzes': quizzes,
        'quiz_details': quiz_details,
        'user': user,
    }
    print(quizzes)
    # print(aiken_quiz)

    if not quizzes:
        return HttpResponse(
            "<script>alert('Nothing is Scheduled by the TPO!'); window.location='quiz_mode'; </script>"
        )
    else:
        return render(request, 'campus/quiz_list.html', context)


# def quiz_detail(request, id):
#     # question = AikenQuizFormat.objects.filter(id=id)
#     # attempts = AikenFile.objects.filter(id=id).values('attempts').get()['attempts']
#     # print('attempts: ', attempts)
#
#     attempt_counter = Aiken_Result.objects.filter(id=id).values('counter').get()['counter']
#     print(attempt_counter)
#
#     if not attempt_counter:
#         data = AikenFile.objects.get(id=id)
#         print(data)
#         print(id)
#
#         times = AikenFile.objects.filter(id=id).values('time').get()['time']
#         print(times)
#         quiz = Quiz.objects.get(id=id)
#         questions = quiz.question_set.all()
#
#         print('questions : \n', questions)
#         print('Quiz:', quiz)
#
#         context = {
#             'quiz': quiz,
#             'questions': questions,
#             'times': times,
#         }
#         return render(request, 'campus/quiz_details.html', context)
#     else:
#         return HttpResponse(
#             "<script>alert('You have already attended this Quiz'); window.location='/quiz_list'; </script>"
#         )

@user_login_required
def quiz_detail(request, id):
    email = request.session['email']
    # Get the quiz and its questions from the AikenFile model
    quiz = Quiz.objects.get(id=id)
    questions = quiz.question_set.all()
    times = AikenFile.objects.filter(id=id).values('time').get()['time']
    start_date = AikenFile.objects.filter(id=id).values('start_date').get()['start_date']
    end_date = AikenFile.objects.filter(id=id).values('end_date').get()['end_date']

    # today = datetime.now(local_tz).date()

    print('start: ', start_date, '\nend: ', end_date)
    # Check if the quiz is still active
    if datetime.today().date() > end_date:
        print('if : ', datetime.today().date())
        return HttpResponse("<script>alert('This quiz is longer available from {}!..'); window.location='/quiz_list'; "
                            "</script>".format(
            end_date.strftime('%d-%m-%Y'))
        )
    elif datetime.today().date() < start_date:
        print('else : ', datetime.today().date())
        return HttpResponse(
            "<script>alert('This quiz will only be opened on {}!..'); window.location='/quiz_list'; </script>".format(
                start_date.strftime('%d-%m-%Y'))
        )

    # Get the attempt counter for this quiz and this user
    attempt_counter = Aiken_Result.objects.filter(
        quiz_id=id, email=email
    ).values_list("counter", flat=True).first()

    context = {
        "quiz": quiz,
        "questions": questions,
        "times": times,
    }

    if not attempt_counter:
        # If the user has not attempted the quiz yet, render the quiz details
        return render(request, "campus/quiz_details.html", context)

    # If the user has already attempted the quiz, show an alert message
    else:
        return HttpResponse(
            "<script>alert('Already attended this quiz!..'); window.location='/quiz_list'; </script>"
        )


@user_login_required
def submit_quiz(request, id):
    email = request.session['email']
    user = get_user(request)
    quiz = get_object_or_404(Quiz, pk=id)
    myData = StudentReg.objects.get(email=user.email)
    sid = myData.id
    student = MCAStudentDetails.objects.get(user=sid)
    quiz_name = AikenFile.objects.filter(id=id).values('id').get()['id']
    print('quiz_name: ', quiz_name)
    # counter = AikenFile.objects.filter(id=id).values('attempts').get()['attempts']
    # print('counter: ', counter)
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
        questions_with_answers = []

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
                    questions_with_answers.append({
                        'question': question,
                        'answer': answer,
                        'is_correct': True,
                    })
                else:
                    wrong += 1
                    print('Wrong Answer')
                    questions_with_answers.append({
                        'question': question,
                        'answer': answer,
                        'is_correct': False,
                    })
            else:
                questions_with_answers.append({
                    'question': question,
                    'answer': None,
                    'is_correct': False,
                })
        percent = (score / total) * 100
        print('Total Mark : ', score)
        counter = 1
        print('counter: ', counter)
        r = Aiken_Result(quiz_id=quiz_name, email=email, score=score, quiz_name=quiz_name, time=time,
                         correct=correct, wrong=wrong, percent=percent, total=total, counter=counter)
        r.save()
        print(r)
        pg_per = student.mcaPer
        pg_cgpa = student.mcaAggregateCgpa
        ug_per = student.ugPer
        ug_cgpa = student.ugCgpa
        hse_per = student.hsePer
        sslc_per = student.sslcPer
        print(pg_per, pg_cgpa, ug_per, ug_cgpa, hse_per, sslc_per, percent)
        analysis = placement_prediction(pg_per, pg_cgpa, ug_per, ug_cgpa, hse_per, sslc_per, percent)
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
            'chances': analysis,
            'questions_with_answers': questions_with_answers,
        }
        return render(request, 'campus/quiz_results.html', context)
    return render(request, 'campus/quiz_list.html', {'quiz': quiz})


def sent_message(request):
    return render(request, 'chat_to_admin')


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
    print(y_pred)

    # Evaluate the performance of the model
    from sklearn.metrics import mean_squared_error, r2_score
    print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
    print('Coefficient of determination (R^2): %.2f' % r2_score(y_test, y_pred))
    print('Accuracy : %.2f' % (r2_score(y_test, y_pred) * 100))
    print('prediction: ', y_pred)

    return r2_score(y_test, y_pred) * 100


def chat_to_admin(request):
    email = request.session['email']
    print(email)
    user = StudentReg.objects.get(email=email)
    context = {
        'user': user,
    }
    return render(request, 'campus/chat.html', context)


import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def placement_prediction(pg_per, pg_cgpa, ug_per, ug_cgpa, hse_per, sslc_per, quiz_per):
    print('pg_per: ', pg_per, '\npg_cgpa: ', pg_cgpa, '\nug_per: ', ug_per, '\nug_cgpa: ', ug_cgpa, '\nhse_per: ',
          hse_per, '\nsslc_per: ', sslc_per, '\nquiz_per: ', quiz_per)
    pickle_file = 'static/csv/model.pickle'

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as f:
            model = pickle.load(f)
    else:
        data = pd.read_csv("static/csv/2020-Student-DB.csv")

        X = data.drop("output", axis=1)
        y = data["output"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor(n_estimators=100, random_state=42)

        model.fit(X_train, y_train)

        with open(pickle_file, 'wb') as f:
            pickle.dump(model, f)

    new_student_scores = [pg_per, pg_cgpa, ug_per, ug_cgpa, hse_per, sslc_per, quiz_per]
    prediction = model.predict([new_student_scores])
    print("Placement Prediction: ", prediction[0]*100)

    return prediction[0]*100

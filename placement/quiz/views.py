from datetime import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AikenUploadForm
from .aiken_parser import parse_aiken_file
import os
from io import StringIO
from django.conf import settings
from django.http import HttpResponse
from .models import *


def quiz_mode(request):
    return render(request, 'quiz/quiz_mode.html')


def upload_aiken(request):
    folder = 'quiz/aiken'
    if request.method == 'POST':
        form = AikenUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file
            file = request.FILES['file']
            fs = FileSystemStorage(location=folder)
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            # parse_aiken_file(file)

            # Redirect to the quiz list page
            return render(request, 'quiz/quiz_list.html', {'file_url': file_url})
    else:
        form = AikenUploadForm()
    return render(request, 'quiz/aiken_upload.html', {'form': form})


def import_aiken(request):
    if request.method == 'POST':
        file = request.FILES['aiken_file']  # get the uploaded file from the request
        file_contents = file.read()  # read the contents of the file as bytes
        file_str = file_contents.decode('utf-8')  # decode the bytes into a string

        # create a filename based on the original filename and the current timestamp
        filename = f'{file.name}-{int(time.time())}.txt'

        # construct the full path to the file within the 'aiken_files' directory
        filepath = os.path.join(settings.BASE_DIR, 'quiz', 'aiken_files', filename)

        # create the 'aiken_files' directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # write the file contents to the file
        with open(filepath, 'w') as f:
            f.write(file_str)

        # parse the Aiken-formatted text and create a quiz object
        quiz = parse_aiken_file(StringIO(file_str))

        # save the quiz object to the database
        quiz.save()

        return HttpResponse('Quiz imported successfully!')
    else:
        return render(request, 'import_aiken.html')

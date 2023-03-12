from django import forms

class AikenUploadForm(forms.Form):
    file = forms.FileField(label='Select a file')

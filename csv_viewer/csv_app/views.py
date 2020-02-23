from django.shortcuts import render
from . import forms
from . import process

def index(request):
    file_name = None
    content = None

    if request.method == 'POST':

        form = forms.CSVForm(request.POST, request.FILES)

        if form.is_valid():

            uploaded_file = request.FILES['uploaded']
            file_name = uploaded_file.name
            content = uploaded_file.read().decode('cp1251')
            content = process.parse_csv(content)

    else:

        form = forms.CSVForm()

    return render(request, 'csv_app/index.html', {'form': form, 'file_name': file_name, 'content': content})


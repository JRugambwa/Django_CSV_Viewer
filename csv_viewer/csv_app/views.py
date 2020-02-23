from django.shortcuts import render, redirect
from . import forms
from . import process


def index(request):

    return render(request, 'csv_app/index.html', {'content': process.get_content()})


def upload(request):

    if request.method == 'POST':

        form = forms.CSVForm(request.POST, request.FILES)

        if form.is_valid():

            uploaded_file = request.FILES['uploaded']
            content = uploaded_file.read().decode('cp1251')
            content = process.parse_csv(content)
            process.insert_to_db(content)

            return redirect('/')

    else:

        form = forms.CSVForm()

    return render(request, 'csv_app/upload.html', {'form': form})


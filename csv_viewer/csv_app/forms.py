from django import forms


class CSVForm(forms.Form):

    uploaded = forms.FileField(label='Your file')

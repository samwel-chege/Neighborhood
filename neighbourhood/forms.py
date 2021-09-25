from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label = 'First_name',max_length=30)
    email = forms.EmailField(label='Email')

class AddResidentForm(forms.Form):
    name = forms.CharField(label='Resident name',max_length=100)
    username = forms.CharField(label='username',max_length=100)
    email = forms.EmailField()    
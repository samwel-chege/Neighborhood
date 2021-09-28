from neighbourhood.models import Neighborhood,Post
from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label = 'First_name',max_length=30)
    email = forms.EmailField(label='Email')

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin','residents']    

class AddResidentForm(forms.Form):
    name = forms.CharField(label='Resident name',max_length=100)
    username = forms.CharField(label='username',max_length=100)
    email = forms.EmailField()    

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin','residents']    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')

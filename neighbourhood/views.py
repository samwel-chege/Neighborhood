from django.shortcuts import render
from .email import send_welcome_email
from .models import NewsLetterRecipients
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.http import JsonResponse
# Create your views here.
def home(request):
    if request.method =='POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('home')

    else:
        form = NewsLetterForm()
    return render(request,'index.html', {'letterForm':form})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name = name,email=email)
    recipient.save()
    send_welcome_email(name,email)
    data = {'sucess':'You have been successfully added to mailing list'}
    return JsonResponse(data)              
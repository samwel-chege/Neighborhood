import neighbourhood
from django.shortcuts import redirect, render,get_object_or_404
from .email import send_welcome_email
from .models import Admin, Business, Neighborhood, NewsLetterRecipients, Post, Resident,User
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import AddResidentForm,NeighborhoodForm,AdminProfileForm,PostForm
import random
import string

# Create your views here.
@login_required(login_url='/accounts/login/') 
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

def create_admin(request):
    current_user = request.user
    if request.method == 'POST':
        form = AdminProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False) 
            profile.user = current_user
            profile.save()
        return redirect(create_hood)
    else:
        form = AdminProfileForm()
    return render(request,'create_admin.html',{"form":form}) 

def create_hood(request):
    current_user = request.user
    try:
        admin = get_object_or_404(Admin,id=id)
    except Admin.DoesNotExist:
        raise Http404()

    my_hood = None
    try:
        my_hood = get_object_or_404(Neighborhood,id=id)
    except Neighborhood.DoesNotExist:
        pass

    if my_hood:
        return redirect(home)
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = admin
            hood.save()
        return redirect(add_resident)
    else:
        form = NeighborhoodForm()
    return render(request,'create_hood.html',{"form":form})                    
    
@login_required(login_url='/accounts/login/') 
def add_resident(request,neighborhood_id):
    current_user = request.user
    try:
        admin = get_object_or_404(Admin,id=neighborhood_id)
    except Neighborhood.DoesNotExist:
        raise Http404()
    try:
        my_hood = get_object_or_404(Neighborhood,id=neighborhood_id)
    except Neighborhood.DoesNotExist:
        raise Http404()        

    if request.method =='POST':
        form = AddResidentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = ''.join(random.choices(string.ascii_uppercase  + string.digits,k=8))
            this_resident = User.objects.create_user(username,name,email)
            resident = Resident(user=this_resident,neighbourhood=my_hood,name=name)
            resident.save()

            my_hood.residents = len(Resident.objects.filter(neighbourhood=my_hood))+1
            my_hood.save()

    
        return redirect(home)
    else:
        form =AddResidentForm()
    return render(request,'add_resident.html',{"form":form})    


def update_hood(request):
    current_user = request.user
    try:
        admin = Admin.objects.get(user=current_user)
    except Admin.DoesNotExist:
        raise Http404()
    try:
        my_hood = Neighborhood.objects.get(admin=admin)
    except Neighborhood.DoesNotExist:
        pass

    if request.method == 'POST':
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            my_hood.name = form.cleaned_data['name']
            my_hood.location = form.cleaned_data['location']
            my_hood.save()
        return redirect(home)

    else:
        form = NeighborhoodForm()
    return render(request,'update_hood.html',{"form":form})     


def delete_hood(request):
    current_user = request.user
    try:
        admin = Admin.objects.get(user=current_user)
    except Neighborhood.DoesNotExist:
        raise Http404()

    try:
        my_hood = Neighborhood.objects.get(admin=admin)
    except Neighborhood.DoesNotExist:
        pass
    admin.delete()
    current_user.delete()

    return redirect(home)    

def all_residents(request):
    current_user  =request.user
    try:
        admin = Admin.objects.all()
    except Admin.DoesNotExist:
        raise Http404()
    try:
        my_hood = Neighborhood.objects.all()
    except Neighborhood.DoesNotExist:
        raise Http404()        

    residents = Resident.objects.all()

    return render(request,'all_residents.html',{"residents":residents,"hood":my_hood})                                  


def business(request):
    business = Business.objects.all()
    return render(request, 'business.html',{"business":business})    

def post(request,hood_id):
    posts= Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = posts
            post.user = request.user
            post.save()
            return redirect('/', posts.id)
    else:
        form = PostForm()    

    return render(request,'post.html',{'form':form})    


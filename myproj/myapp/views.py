from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # name = 'Morghan'
    # context = {
    #     'name': 'Morghan',
    #     'age': 23,
    #     'nationality':'American'
    # }
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_trus = True
    # feature1.details = 'Our service is quick'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Smart'
    # feature4.is_trus = False
    # feature4.details = 'Our service is smart'
    
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Cool'
    # feature3.is_trus = True
    # feature3.details = 'Our service is cool'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_trus = True
    # feature2.details = 'Our service is reliable'
    # features = [feature1, feature2, feature3, feature4]

    # can erase thos ebaove bc they shd all now be in the admin db site. I must have done smth wrong bc I can't add features to mine but i can't figure out why
    
    
    features = Feature.objects.all() #gets them from the db

    return render(request, 'index.html', {'features': features})# context) #last param is for sending in dynamic data

def counter(request):
    text = request.POST['text'] #its getting the textarea in index.html bc its name is text and storing the text in this var. make sure the post/get matches w wats in whatever is sending to it
    num_words = len(text.split())
    return render(request, 'counter.html', {'num': num_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords different')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: #means it is not on our platform
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(req):
    auth.logout(req)
    return redirect('/')

    #save to the db
    return render(request, 'register.html')
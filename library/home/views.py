from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'home/contact.html')

def handelSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous input
        # username shoud be under 10 characters
        if len(username) > 10:
            messages.error(
                request, 'username most be under 10 characters .')
            return redirect('home')

        # username shoud be alphanumeric
        if not username.isalnum():
            messages.error(
                request, 'username shoud only contain Alphabats and Numbers .')
            return redirect('home')

        # Password shoud be minimem 10 characters
        if len(pass1) <= 10:
            messages.error(
                request, 'Password Shoud be minimem 10 characters .')
            return redirect('home')

        # password matching
        if pass1 != pass2:
            messages.error(
                request, 'Password do not match . Please try agin .')
            return redirect('home')

        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, 'Your AIscintest Account Is Successfully Created .')
        return redirect('home')
    else:
        return HttpResponse("404 - User Not Found")


def handelLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(
                request, 'Successfully Logged In .')
            return redirect('home')
        else:
            messages.error(
                request, 'Invalid Credentials, Please Try Again .')
            return redirect('home')

    return HttpResponse("404 - Not Found")


def handelLogout(request):
    logout(request)
    messages.success(
        request, 'Successfully Logged Out .')
    return redirect('home')
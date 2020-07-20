from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    #return HttpResponse("<h1>Hello Ajay</h1>")
    return render(request, 'index.html')


def contact(request):
    
    return render(request, 'contact.html')

def ajay(request):
    
    return render(request, 'ajay.html')

def handleSignup(request):
    if request.method == 'POST':
        #GEt the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        #messages.success(request, "Your iCoder account has been successfully created")
        return redirect('/')

def handleLogin(request):
      if request.method == 'POST':
        #GET the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            #messages.success(request, "Successfully Logged IN")
            return render(request, 'login.html')
        else:
            #messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')
    
      return HttpResponse('404 - Not Found')

def handleLogout(request):
    
    logout(request)
    #messages.success(request, "Successfully Logged Out")
    return redirect('/')
    
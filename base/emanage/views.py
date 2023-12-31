from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "home.html", {})

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request,("Login Successfully....."))
            return redirect('home')
        else:
            messages.success(request, ("There was an error in logging in, Try Again...!"))
            return redirect('login')
    else:
        return render(request, "login.html", {})
   
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None:
                messages.success(request,("Registration Successfull"))
                return redirect('login')
            else:
                return redirect('register')
    else:
        form = UserCreationForm()
            
    return render(request, 'register.html', {'form':form})
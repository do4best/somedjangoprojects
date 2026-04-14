from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from todo import models


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user = User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(emailid,pwd)
        user = authenticate(request,username=emailid,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('todoapp')
        else:
            return render(request,'login')


    return render(request,'login.html')

def todoapp(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOAPP(title=title,user=request.user)
        obj.save()
    return render(request,'todoapp.html')
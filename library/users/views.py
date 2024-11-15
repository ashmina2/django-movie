from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from users.models import Users
from django.contrib.auth.decorators import login_required

@login_required
def view_users(request):
    k=Users.objects.all()        #reads all records from the book table
    context={'users':k}          #sends data from view function to html page


    return render(request,'view_users.html',context)


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==cp):
            user=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return redirect('books:home')
        else:
            return HttpResponse("Passwords are not same")

    return render(request,'adminregister.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user: #if matching user exits
            login(request,user)
            return redirect('books:home')
        else:  #if no matching user
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')

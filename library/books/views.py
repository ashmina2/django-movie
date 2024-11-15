from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from books.models import Book

def home(request):
    return render(request,'home.html')

@login_required
def viewbooks(request):
    #k=con.execute('select * from Book')
    #k=modelname.objects.all()

    k=Book.objects.all()        #reads all records from the book table
    context={'book':k}          #sends data from view function to html page
    return render(request,'view.html',context)

@login_required
def addbooks(request):
    if(request.method=='POST'): # form kodutha name vech oronnum POST koduthu
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        i=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=i,pdf=f)
        b.save()

        return viewbooks(request)

    return render(request,'add.html')

@login_required
def bookdetails(request,p):

    k=Book.objects.get(id=p)  #reads a particular record
    context={'book':k}      #html pagilotte context vazhi aane display avunne

    return render(request,'details.html',context)

@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('books:viewbooks')

@login_required
def edit(request,p):

    k=Book.objects.get(id=p)
    if(request.method=='POST'):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price= request.POST['p']
        k.pages = request.POST['pa']
        k.language = request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')
        if (request.FILES.get('f') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('f')

        return redirect('books:viewbooks')

    context={'book':k}
    return render(request,'edit.html',context)
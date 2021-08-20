from django.shortcuts import render,HttpResponse
from Home.models import Contacts
# Create your views here.
def nav(request):
    return render(request,'nav.html')
def home(request):
    #return HttpResponse("This is my Home Page")
    context = {'name':'Harry','course':'Django'}
    return render(request, 'home.html',context)
def about(request):
    #return HttpResponse("This is about page(/about)")
    return render(request, 'about.html')
def projects(request):
    #return HttpResponse("This is projects page(/projects)")
    return render(request, 'projects.html')
def contact(request):
    if request.method=="POST":
        print("This is posts")
        Name = request.POST['Name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(Name,email,phone,desc)
        contact = Contacts(Name=Name,email=email,phone=phone)
        contact.save()
        print("The data has been written to the DataBase")
    return render(request,'contact.html')
from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')
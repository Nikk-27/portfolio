from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    #return HttpResponse("This is my homepage (/home)")
    return render(request, '/index.html')
def home(request):
    #return HttpResponse("This is my homepage (/home)")
    #context = {'name':'nikk','course':'django'}
    #return render(request, 'home.html',context)
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("This is my abouts page (/about)")
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        print("This is post.")
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]
        print(name,email,phone,desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("Data save successfully.")
    #return HttpResponse("This is my contact page (/contact)")
    return render(request, 'contact.html')
def projects(request):
    #return HttpResponse("This is my projects page (/project)")
    return render(request, 'project.html')


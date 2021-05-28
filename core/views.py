from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from core.models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sendMassage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        massage = request.POST.get('massage')
    c = Contact(name='name', email='email', subject='subject', massage='massage')
    c.save()
        
    return HttpResponseRedirect('/')


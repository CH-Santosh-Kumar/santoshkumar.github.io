from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# Create your views here.
@csrf_exempt
def home(request):
    name = request.POST.get('name','')
    email = request.POST.get('email','')
    to = ['chsantoshkumar802@gmail.com','therappinpoet@gmail.com']
    subject = str(request.POST.get('subject','') + " : " + name + " Email ID: " + email)
    message = request.POST.get('message','')
    
    if request.method == 'POST' and email and name:
        send_mail(subject,message,email,to,fail_silently = False)
        return render(request,'home.html',{'name': name})
    else:
        return render(request,'home.html',{})


import smtplib
import ssl

from django.shortcuts import render
from.models import UserRegister

# Create your views here.
def Registration(request):
    name=request.POST.get("name")
    contact=request.POST.get("contact")
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(name,contact,email,username,password)
    smtp_server = "smtp.gmail.com"
    import smtplib
    email_from = "prasadnaidu766@gmail.com"
    email_to = email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, "cnjvwtoprlhfaqzj")
    message = "Hi " + name + " You are registered Our Application "
    server.sendmail(email_from, email_to, message)
    server.quit()
    UserRegister(name=name, contact=contact, email=email, username=username, password=password).save()
    return render(request,"register.html",{"message":"Successfully Registred"})


def Login_Details(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    qs=UserRegister.objects.filter(username=username,password=password)
    if qs:
        return render(request,"Welcome.html",{"name":username})
    else:
        return render(request,"register.html",{"message":"Invalid Details"})
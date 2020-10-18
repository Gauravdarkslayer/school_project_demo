from django.shortcuts import render
from .models import user
# Create your views here.
def login_page(request):
    return render(request,'login.html')

def login(request):
    email = request.POST["email"]
    password= request.POST["password"]
    if user.objects.filter(email_id=email).exists():
        print(user.objects.filter(email_id=email).values('password')[0]['password'])
        if user.objects.filter(email_id=email).values('password')[0]['password'] == password:
            print("ot hgere")
            return render(request,"choose.html")
        else:
            
            return render(request,"login.html",{"message":"invalid credentials"})
    else:
        return render(request,"login.html",{"message":"doesnt exists"})

def signup_page(request):
    return render(request,"signup.html")

def signup(request):
    full_name = request.POST["full_name"]
    email = request.POST["emailid"]
    password= request.POST["password"]

    if user.objects.filter(email_id=email).exists():
        return render(request,"signup.html",{"message":"already exists"})

    user.objects.create(full_name=full_name, email_id=email,password=password)
    return render(request,"login.html")


def choose(request):
    return render(request,"choose.html")
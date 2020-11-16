from django.shortcuts import render
from .models import user
from django.http import HttpResponseRedirect
# Create your views here.
# def login_page(request):
#     return render(request,'signin.html')

def login(request):
    if request.method.lower() == "post":
        email = request.POST["email"]
        password= request.POST["password"]
        print(request.POST["email"],request.POST["password"])
        if user.objects.filter(email_id=email).exists():
            print(user.objects.filter(email_id=email).values('password')[0]['password'])
            if user.objects.filter(email_id=email).values('password')[0]['password'] == password:
                print("ot hgere")
                return HttpResponseRedirect('/test_gen/')
            else:
                
                return render(request,"signin.html",{"message":"invalid credentials"})
        else:
            return render(request,"signin.html",{"message":"doesnt exists"})

    else:
        return render(request,'signin.html')

def signup_page(request):
    return render(request,"signup.html")

def signup(request):
    full_name = request.POST["full_name"]
    email = request.POST["emailid"]
    password= request.POST["password"]
    print("I am inside down")

    if user.objects.filter(email_id=email).exists():
        print("alreay exists")
        return render(request,"signup.html",{"message":"already exists"})

    user.objects.create(full_name=full_name, email_id=email,password=password)
    return render(request,"signin.html")


def choose(request):
    return render(request,"choose.html")


def homepage(request):
    return render(request, 'index.html')
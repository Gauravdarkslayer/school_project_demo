from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'login.html')

def login(request):
    email = request.POST["emailid"]
    password= request.POST["password"]
    if user.objects.filter(email=email).password == password:
        user.objects.create(full_name=full_name, email=email,password=password)
    else:
        return render(request,"login.html",{"message":"invalid credentials"})
    return render(request,"homepage.html")

def signup_page(request):
    return render(request,"signup.html")

def signup(request):
    full_name = request.POST["full_name"]
    email = request.POST["emailid"]
    password= request.POST["password"]

    if user.objects.filter(email=email).exists():
        return render(request,"signup.html",{"message":"already exists"})

    user.objects.create(full_name=full_name, email=email,password=password)
    return render(request,"login.html")



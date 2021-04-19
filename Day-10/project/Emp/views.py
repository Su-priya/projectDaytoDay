from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def cont(request):
	return render(request,'html/cont.html')

def login(request):
	return render(request,'html/login.html')

def register(request):
	return render(request,'html/register.html')

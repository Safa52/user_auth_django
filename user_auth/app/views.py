from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


def register_view(request):
    context={}
    if request.user.is_authenticated:
        return render(request,'login.html',{'error':'already registered'})

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=User.objects.get(username=username)
            context={'error':'username already exist'}
        except:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('login')      
    return render(request,'register.html',context)
    




def login_view(request):
    context={}
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'usename or password incorrect'})
        
            
    return render(request,'login.html')
        
    
    

def home_view(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            logout(request)
            return redirect('login')

        return render(request,'home.html',{'message':'Successfully loggedin'})
    
    else:
        return render(request,'login.html',{'error':'login first'})
    


        

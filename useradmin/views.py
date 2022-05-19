from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def home(request):
   return render(request , 'back/home.html')



def login_user(request):
   #if not request.user.is_authenticated: return redirect('login_user')
   message = None
   if request.method  == 'POST' :

        username=request.POST['username']
        password=request.POST['password']

        #username=request.POST.get('username')
        #password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None : 

            login(request, user)
            return redirect('loginindex')  

        else:

            message = 'نام کاربری یا رمز عبور اشتباه است'
            return render(request, 'back/login.html', {'message':message})


   return render(request, 'back/login.html')
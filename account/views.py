from datetime import timezone
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
   return render(request , "front/index.html" ) 

def newLogin(request):
   
  message = None
  if request.method  == 'POST' :

        username=request.POST['username']
        password=request.POST['password']

        #username=request.POST.get('username')
        #password=request.POST.get('password')
        print(username , password)
        user = authenticate(username=username, password=password)
        
        if user is not None : 

            login(request, user)
            return redirect('loginindex')  

        else:
            message = 'نام کاربری یا رمز عبور اشتباه است'
            return render(request, 'front/newLogin.html', {'message':message})


  return render(request, 'front/newLogin.html')



def signup_user (request):
    messages=None
    if request.method =="POST" :
        #user = authenticate(username=request.POST['username'], password=request.POST['password'])
        username=request.POST['username']
        password=request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages = 'این نام کاربری قبلا ثبت شده است'
                return redirect(request , 'index' )
        
            else:
                user = User.objects.create_user(username=username, password=password )
                                       
                user.save()
                
                return redirect("loginindex")


        else:
            messages = 'تکرار رمزعبور مطابقت ندارد'
            return redirect(request,'signup_user' )
            

    else:
        return render(request, "front/signup.html")


def logout_user(request):
    logout(request)
    return redirect('index')        


def loginindex(request):
   return render(request , 'front/loginindex.html')

def user_list(request):
    users=User.objects.all()
    return render(request, 'back/users.html',  {'users': users})

   
def profile(request):
    return render(request , "front/profile.html")


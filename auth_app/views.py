from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    # if request.method == "POST":
    #     data = contact()
    #     full_name = request.POST.get('full_name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')

    #     data.full_name = full_name
    #     data.email = email
    #     data.message = message
    #     data.save()
    #     messages.success(request, 'Successfull your send Message !')
    #     return redirect('contact')

    return render(request, 'contact.html')
    


def register(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        new_user = User.objects.create_user(username=username, email=email, password=password1)
        new_user.save()
        return redirect('login')

    return render(request, 'register.html')





def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('messages')
        

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
  


def messages(request):
    return render(request, 'messages.html')

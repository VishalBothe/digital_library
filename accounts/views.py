from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import login,logout,authenticate

from .forms import SignInForm,SignUpForm

import json
# Create your views here.

def signup(request):
    if request.method == "POST":
        # This block is handling the ajax request
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password1']

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, "Email alredy Registered!!")
            return redirect('/accounts/signup')

        user = CustomUser(
            name=name,
            email=email,
            mobile=mobile,
        )
        user.set_password(password)
        try:
            user.save()
            response = {"message":"User created", "status":200}

            return HttpResponse(json.dumps(response))
            
        except Exception as e:
            print("USER NOT CREATED:",e)
            return HttpResponse({
                "message":"Failed to create user",
                "status":400
            })
    else:
        signUpForm = SignUpForm()
        return render(
            request,
            'accounts/register.html',
            {'signUpForm':signUpForm}
        )

def signin(request):
    if request.method == "POST":
        signInForm = SignInForm(request.POST)

        if signInForm.is_valid():
            email = signInForm.cleaned_data['email']
            password = signInForm.cleaned_data['password']

            user = authenticate(email=email,password=password)
            if user is None:
                messages.info(request,"Invalid credentials!!")
                return redirect('signin')
            login(request, user)
            return redirect('/enrollment/mybooks')
        else:
            messages.info(request, "Invalid Data!!")
            return redirect('/accounts/signin')

    signInForm = SignInForm()
    return render(request, 'accounts/signin.html', {'signInForm':signInForm})

def signout(request):
    logout(request)
    return redirect('signin')
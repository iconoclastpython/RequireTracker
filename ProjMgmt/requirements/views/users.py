from django import forms
import requirements.models.user_manager
from requirements.models import user_manager
from django.http import HttpResponse, HttpResponseRedirect
from forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

def create_user(request):
	if userManager.createUser(request) :
		return HttpResponse("Your request has been submitted. It will need to be approved by an administrator.")
	else:
		#TODO refactor to use @user_passes_test
		return HttpResponse("Failed to create user")


def members(request):
    return render(request, 'Members.html')

def registration(request):
    if request.method =='POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            user_manager.createUser(request)
            return HttpResponseRedirect('/thankYou/')
    else:
        form =  RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def thank_you(request):
    return render(request, 'ThankYou.html')

def signin(request):
    logout(request)
    username = password = ''
    errormsg = ""
    next = ""
    
    if request.GET:
        next = request.GET['next']
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next == '':
                    return HttpResponseRedirect('/projects')
                else:
                    return HttpResponseRedirect(next)
        else:
            errormsg = 'Username or Password is incorrect ! Please try again !'
    return render_to_response('SignIn.html', 
                              {'errorMsg': errormsg, 'next': next, 'isUserSigningInUpOrOut': 'true'}, 
                              context_instance=RequestContext(request))

def signup(request):
    if request.method =='POST':
        form =  RegistrationForm(request.POST)
        if form.is_valid():
            # This is where you do stuff and then go to thank you page
            user_manager.createUser(request)
            return render(request,'SignUpFinish.html',{'form': form, 'isUserSigningInUpOrOut': 'true'})
    else:
        form =  RegistrationForm()
        return render(request, 'SignUp.html', {'form': form, 'isUserSigningInUpOrOut': 'true'})
    
@login_required    
def signout(request):
    logout(request)
    context = {'isUserSigningInUpOrOut': 'true'}
    return render(request, 'SignOut.html', context)
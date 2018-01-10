from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def landing(request):
	if request.user.is_authenticated():
		#return render(request, 'landing.html')
		return redirect('/home')
	else:
		return render(request, 'landing.html')
			

def signin(request):
	return render(request, 'login.html')	

def registerView(request):
	if request.method == 'POST':
		post = request.POST

		email = post.get('email')
		password1 = post.get('pass')
		password2 = post.get('cpass')
		username = getUsername(email)

		if password1 != password2:
			messages.warning(request, "passwords do not match", fail_silently=True)
			return render(request, 'login.html')

    	user = User.objects.create_user(username=username, email=email)
    	user.set_password(password1)
    	user.save()
    	return render(request,'home.html')

def loginView(request):
	if request.method == 'POST':
		#user = request.user
		post = request.POST
		email = post['email']
		password = post['pass']
		username = getUsername(email)
		user = authenticate(username=username, email=email, password=password)

		if user is not None:
			login(request, user)
			return render(request,'home.html')


def getUsername(email):
    email = str(email)
    index = email.index('@')

    answer = email[:index]
    return answer

def home(request):
    if request.user.is_authenticated():
        return render(request,'home.html')
    else:
        return redirect("/login")  

# def ad(request):
# 	if request.method=='POST':
# 		post=request.POST
# 		email = post.get('email')
# 		password1 = post.get('pass')
# 		password2 = post.get('cpass')
# 		username = getUsername(email)
# 	return render(request,'formpage.html')


def logoutView(request):
	logout(request)
	return render(request, 'landing.html')	

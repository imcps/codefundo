from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def landing(request):
	return render(request, 'landing.html')

def login(request):
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
		post = request.POST
		email = post['email']
		password = post['pass']
		username = getUsername(email)
		user = authenticate(username=username, email=email, password=password)

		if user is not None:
			return render(request,'home.html')


def getUsername(email):
    email = str(email)
    index = email.index('@')

    answer = email[:index]
    return answer

def home(request):
    # if request.user.is_authenticated():
         return render(request,'home.html')
    # else:
    #      return redirect("/login")  

def ad(request):
	return render(request,'ad.html')

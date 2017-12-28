from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
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
			message.warning(request, "passwords do not match", fail_silently=True)
			return render(request, 'login.html')

    	user = User.objects.create_user(username=username, email=email)
    	user.set_password(password1)
    	user.save()
    	return HttpResponse('<h1>SUCCESS !!</h1>')

def loginView(request):
	if request.method == 'POST':
		post = request.POST
		email = post['email']
		password = post['pass']
		username = getUsername(email)
		user = authenticate(username=username, email=email, password=password)

		if user is not None:
			return HttpResponse('<h1>login Success</h1>')


def getUsername(email):
	return "user"

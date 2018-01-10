from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

def postAd(request):
	if request.method == 'GET':
		return render(request, 'postad.html')
	elif request.method == 'POST':
		post = request.POST
		ad = Advertisment()

		ad.user = request.user
		ad.title = post.get('title')
		ad.category = post.get('category')
		ad.description = post.get('description')
		ad.name = post.get('name')
		ad.mobileNumber = post.get('number')
		ad.hostel = post.get('hostel')
		ad.room = post.get('room')

		ad.save()

		return HttpResponse("<h1>Ad posted Successfully!</h1>")



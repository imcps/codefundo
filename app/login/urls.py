from django.conf.urls import url
from views import *


app_name = 'login'

urlpatterns = [
	url(r'^$', login, name='login'),
	url(r'^login/$', loginView, name='loginView'),
	url(r'^register/$', registerView, name='registerView'),
]
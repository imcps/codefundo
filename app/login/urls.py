from django.conf.urls import url
from views import *


app_name = 'login'

urlpatterns = [
	url(r'^$', login, name='login'),
]
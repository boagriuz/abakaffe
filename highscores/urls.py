from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.get_monthly_highscore, name = 'get_monthly_highscore'),
]
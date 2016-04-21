from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.brewer_post, name = 'brewer_post'),
]
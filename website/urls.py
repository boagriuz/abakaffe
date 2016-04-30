from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^highscore/$', views.highscore, name='highscore'),
    url(r'^about/$', views.about, name='about'),

]

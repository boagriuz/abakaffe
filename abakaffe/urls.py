"""abakaffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'website'
app_name = 'update'

urlpatterns = [
<<<<<<< HEAD

    url(r'^', include('website.urls')),
=======
    url(r'^update/', include('update.urls')),
    url(r'^website/', include('website.urls')),
>>>>>>> c54d0056b178464785922064ba91e5815db6c45e
    url(r'^admin/', admin.site.urls),
]

#check if DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


"""WhatsIM URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from IMapp import views as index_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_views.index),
    url(r'^login/', index_views.login),
    url(r'^loggedin/', index_views.loggedin),
    url(r'^register/', index_views.register),
    url(r'^logout/', index_views.logout),
    url(r'^check_username/', index_views.check_username),
    url(r'^check_passwd/', index_views.check_passwd),
]

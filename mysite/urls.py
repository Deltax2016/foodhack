
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^search/$', views.search),
    url(r'^api/register$', views.reg),
    url(r'^api/friends$', views.friends),
    url(r'^api/like$', views.like),
    url(r'^api/near$', views.near),
    url(r'^api/gps$', views.gps),
    url(r'^stop$', views.gps),

]

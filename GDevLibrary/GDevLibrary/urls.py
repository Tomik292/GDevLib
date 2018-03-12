"""
Definition of urls for GDevLibrary.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.contrib.auth import views as build_views

import app.forms
import app.views as views

from django.conf.urls import include
from django.contrib import admin

urlpatterns = [ 

    # /
    url(r'^$',
       views.home,
       name='home'),

    # /login/
    url(r'^login/$',
        views.UserLoginView,
        name='login'),

    #redirects to /login/
    url(r'^logout/$',
        build_views.logout,
        {'next_page':'login'},
        name='logout'),

    # /register/
    url(r'^register/$',
        views.UserRegisterView,
        name='register'),

    # /unity/
    url(r'^unity/',
       views.main_unity,
       name='main_unity'),
    
    # /cry/
    url(r'^cry/',
       views.main_cry,
       name='main_cry'),
   
    # /unreal/
    url(r'^unreal/',
       views.main_unreal,
       name='main_unreal'),


    # /account/
    url(r'^account/',
        views.account,
        name='account'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # /admin/
    url(r'^admin/', admin.site.urls),
]

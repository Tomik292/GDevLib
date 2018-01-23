"""
Definition of urls for GDevLibrary.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views as views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [ 

    # /
    url(r'^$',
       views.home,
       name='home'),

    # /login/
    url(r'^login/$',
        views.login,
        name='login'),

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


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # /admin/
    url(r'^admin/', include(admin.site.urls)),
]

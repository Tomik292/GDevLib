"""
Definition of urls for GDevLibrary.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static

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

    #/user/id
    #url(r'^user/id(?P<id>\d+)/',
    #    views.user_view,
    #    name='user_view'),

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


    # /account/profile/
    url(r'^account/profile/$',
        views.account,
        name='account'),

     # /account/messages
    url(r'^account/messages/$',
        views.messages,
        name='messages'),

    # /account/messages/1 
    url(r'^account/messages/msg(?P<id>\d+)/$',
        views.message_detail,
        name='message_detail'),

    # /account/send_message/
    url(r'^account/send_message/$',
        views.message_form,
        name='message_form'),

     # /account/articles
    url(r'^account/articles/$',
        views.articles,
        name='articles'),

         # /account/articles
    url(r'^account/articles/(?P<article_id>[0-9]+)/$',
        views.article_detail,
        name='article_detail'),

    url(r'^account/create_article/$',
        views.create_article,
        name='create_article'),

     # /account/favorites
    url(r'^account/favorites/$',
        views.favorites,
        name='favorites'),

     # /account/settings
    url(r'^account/settings/$',
        views.settings,
        name='settings'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # /admin/
    url(r'^admin/', admin.site.urls),


]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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

    # user authetication
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
     
    # Defualt page and engine pages
    # /
    url(r'^$',
       views.home,
       name='home'),

    # /unity/
    url(r'^unity/$',
       views.main_unity,
       name='main_unity'),
    
    # /cry/
    url(r'^cry/$',
       views.main_cry,
       name='main_cry'),
   
    # /unreal/
    url(r'^unreal/$',
       views.main_unreal,
       name='main_unreal'),

    # /other/
    url(r'^other/$',
        views.main_other,
        name='main_other'),


    #Logged in user pages

    # /account/profile/
    url(r'^account/profile/$',
        views.account,
        name='account'),

     # /account/messages
    url(r'^account/messages/$',
        views.messages,
        name='messages'),

    # /account/messages/msg[number] 
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

    url(r'account/articles/(?P<article_id>[0-9]+)/delete/$',
        views.delete_article,
        name='delete_article'),

    # /articles/[number]
    url(r'^articles/(?P<article_id>[0-9]+)/$',
        views.article_detail,
        name='article_detail'),

    # /account/create_article/tag
    url(r'^account/create_article_tag/$',
        views.create_article_tag,
        name='create_article_tag'),

    # /account/create_article/html
    url(r'^account/create_article_html/$',
        views.create_article_html,
        name='create_article_html'),

     # /account/settings
    url(r'^account/settings/$',
        views.settings,
        name='settings'),

    url(r'^account/settings/change_password/$',
        views.password_change,
        name="password_change"),

     #/user/id
    url(r'^user/(?P<username>[\w.@+-]+)/$',
        views.user_view,
        name='user_view'),

    url(r'^account/create_article_saved/(?P<article_id>[0-9]+)/$',
        views.create_article_saved,
        name='create_article_saved'),

    url(r'^articles/(?P<article_id>[0-9]+)/verified/$',
        views.verify_article,
        name='verify_article'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # /admin/
    url(r'^admin/', admin.site.urls),


]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
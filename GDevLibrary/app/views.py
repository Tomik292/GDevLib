from datetime import datetime

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.mail import send_mail

from .forms import UserForm, LoginForm, MessageForm, ArticleForm, UserExtensionForm
from .utils import UserCheck
from .models import Message, Article

def UserRegisterView(request):
    u = UserCheck(request)
    template_name = 'app/register.html'
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False) 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            send_mail(
             'Welcome to GDevLibrary',
             'Click on this lick for your email authetizatation',
             settings.EMAIL_HOST_USER,
              [email, settings.EMAIL_HOST_USER],
              fail_silently = False
             )

            return redirect('login')
    else:
        form = UserForm()

    content= {
        'form':form,
        'user':u 
        }

    return render(request, template_name, content)

def UserLoginView(request):
    u = UserCheck(request)
    template_name = 'app/login.html'
    if request.method ==  'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
    else:
        form = LoginForm()
    content= {
        'form':form,
        'user':u
        }

    return render(request, template_name, content)

def account(request):
    """Renders the home page."""
    u = UserCheck(request)
    return render(
        request,
        'app/account.html',
        {'user':u})

def messages(request):
    """ Renders the messages page """
    u = UserCheck(request)

    sent_msgs = Message.objects.filter(sender = u)

    delivered_msgs = Message.objects.filter(recipient = u.username)

    not_seen_msgs = Message.objects.filter(recipient = u.username, seen = False)

    print(not_seen_msgs.count())

    context = {
        'user':u,
        'sent':sent_msgs,
        'delivered':delivered_msgs,
        'not_seen':not_seen_msgs,
        }

    return render(
        request,
        'app/messages.html',
        context
        )

def message_detail(request, id):
    u = UserCheck(request)
    message = get_object_or_404(Message, pk=id)
    message.seen = True
    message.save()

    context = {
        'user':u,
        'message':message
        }

    return render(
        request,
        'app/message.html',
        context)

def message_form(request):
     u = UserCheck(request)
     if request.method ==  'POST':
        form =  MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                sender = u,
                recipient = form.cleaned_data['recipient'],
                subject = form.cleaned_data['subject'],
                text = form.cleaned_data['text'],
                sedingTime = datetime.now(),
                )
            return redirect('messages')
     else:
        form = MessageForm()

     context = {
        'user':u,
        'form':form,
        }
    
     return render(
        request,
        'app/message_form.html',
        context)



def settings(request):
    """ Renders the settings page """
    u = UserCheck(request)
    form = UserExtensionForm(request.POST or None, instance = u)
    if form.is_valid():
        form.save()
        return redirect('account')
    
    context = {
        'user':u,
        'form':form,
        }

    return render(
        request,
        'app/settings.html',
        context)

#def user_view(request, id):
#     u = get_object_or_404(User, id=id)

#     context = {
#         'user': u,
#         }
    
#    # return redirect(reverse('u', kwargs={'id': u.id}))
    
#    #return render(
#    #     request, 
#    #     'app/user_page.html',
#    #     context)


def articles(request):
    """ Renders the articles page """
    u = UserCheck(request)
    saved_art = Article.objects.filter(user = u, released = False) 
    released_art = Article.objects.filter(user = u, released = True) 

    context = {
            'saved':saved_art,
            'released':released_art,
            'user':u,
        }

    return render(
        request,
        'app/articles.html',
        context)

def create_article(request):
    u = UserCheck(request)
    form =  ArticleForm(request.POST or None, request.FILES or None)
    if 'CREATE' in request.POST:
        if form.is_valid():
            Article.objects.create(
                user = u,
                name = form.cleaned_data['name'],
                engine = form.cleaned_data['engine'],
                picture = form.cleaned_data['picture'],
                text = form.cleaned_data['text'],
                tags = form.cleaned_data['tags'],
                # picture = form.cleaned_data['picture'],
                verified = False,
                released = True,
                release_date = datetime.now(),
                )
            return redirect('articles')
    if 'SAVE' in request.POST:
        if form.is_valid():
            Article.objects.create(
                user = u,
                name = form.cleaned_data['name'],
                engine = form.cleaned_data['engine'],
                picture = form.cleaned_data['picture'],
                text = form.cleaned_data['text'],
                tags = form.cleaned_data['tags'],
                # picture = form.cleaned_data['picture'],
                verified = False,
                released = False,
                release_date = datetime.now(),
                )
            return redirect('articles')

    context = {
        'user':u,
        'form':form,
        }

    return render(
        request,
        'app/article_form.html',
        context)

def article_detail(request, article_id):
    u = UserCheck(request)

    template = loader.get_template('app/article.html')

    article = get_object_or_404(Article, pk=article_id)

    context = {
         'user':u,
         'article':article
         }

    return render(
         request,
         'app/article.html',
         context
         )

def favorites(request):
    """ Renders the favorites page """
    u = UserCheck(request)
    return render(
        request,
        'app/favorites.html',
        {'user':u})


def home(request):
    """Renders the home page."""
    u = UserCheck(request)

    return render(
        request,
        'app/main.html',
        {'user':u})

def main_unity(request):
    u = UserCheck(request)
    return render(
        request,
       'app/unity_main.html',
       {'user':u})

def main_unreal(request):
    u = UserCheck(request)
    return render(
        request,
        'app/unreal_main.html',
        {'user':u})

def main_cry(request):
    u = UserCheck(request)
    return render(
        request,
       'app/cry_main.html',
       {'user':u})

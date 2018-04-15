from datetime import datetime

from django.conf import settings as conf_settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.generic import View
from django.core.mail import EmailMessage

from .tokens import account_activation_token
from .forms import *
from .utils import UserCheck, MakeHTML, filter_articles
from .models import Message, Article, Comment


def UserRegisterView(request):
    u = UserCheck(request)
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_active = False
            user.save()

            user_email = form.cleaned_data['email']

            current_site = get_current_site(request)
            mail_subject = "Welcome to GDevlibrary"
            message = render_to_string('app/acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
                })
            email = EmailMessage(
                    mail_subject, message, to=[user_email]
                )
            email.send()
            
            return HttpResponse('Please confirm your email adress to comeplete registration')
    else:
        form = UserForm()

    content= {
        'form':form,
        'user':u 
        }

    return render(request, 'app/register.html', content)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

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

#Engine pages ------------------------------------------------

def home(request): 
    """Renders the home page."""
    u = UserCheck(request)

    context = { 
            'user':u,
        }

    return render(
        request,
        'app/main.html',
        context)

def main_unity(request):
    u = UserCheck(request)

    if request.method ==  'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            key_words = form.cleaned_data['key_words']
        
        articles = filter_articles(key_words,"UNITY")

        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/unity_main_search.html',
            context)

    else:
        form = SearchForm()
        articles = Article.objects.filter(engine = "UNITY")[:16]
        
        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/unity_main.html',
            context)


def main_unreal(request):
    u = UserCheck(request)

    if request.method ==  'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            key_words = form.cleaned_data['key_words']

        articles = filter_articles(key_words,"UNREAL")

        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/unreal_main_search.html',
            context)

    else:
        form = SearchForm()
        articles = Article.objects.filter(engine = "UNREAL")[:16]
        
        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/unreal_main.html',
            context)

def main_cry(request):
    u = UserCheck(request)

    if request.method ==  'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            key_words = form.cleaned_data['key_words']
        
        articles = filter_articles(key_words,"CRY")

        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/cry_main_search.html',
            context)

    else:
        form = SearchForm()
        articles = Article.objects.filter(engine = "CRY")[:16]
        
        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/cry_main.html',
            context)

def main_other(request):
    u = UserCheck(request)

    if request.method ==  'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            key_words = form.cleaned_data['key_words']

        articles = filter_articles(key_words,"OTHER")

        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/other_main_search.html',
            context)

    else:
        form = SearchForm()
        articles = Article.objects.filter(engine = "OTHER")[:16]
        
        print(articles)

        context = { 
            'user':u,
            'articles':articles,
            'form':form,
            }

        return render(
            request,
            'app/other_main.html',
            context)

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

    user_data = {'username':u.username,
                 'first_name':u.first_name,
                 'last_name':u.last_name,
                 'email':u.email,
                 'bio':u.userextension.bio,
                 'location':u.userextension.location}

    form = UserExtensionForm(request.POST or None, initial = user_data)
    if form.is_valid():
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        bio = form.cleaned_data['bio']
        location = form.cleaned_data['location']

        if form.has_changed:
            if not User.objects.filter(username = username).exists() or u.username == username:
                u.username = username
            u.first_name = first_name
            u.last_name = last_name
            u.email = email
            u.userextension.bio = bio
            u.userextension.location= location
            u.save()

        return redirect('account')
    
    context = {
        'user':u,
        'form':form,
        }

    return render(
        request,
        'app/settings.html',
        context)

def password_change(request):
    u = UserCheck(request)

    form = ChangePasswordForm(request.POST or None)
    if form.is_valid():
        new_password = form.cleaned_data['new_password']
        new_password_again = form.cleaned_data['new_password_again']

        u.set_password(new_password)
        u.save()
        return redirect('logout')

    context = {
        'user':u,
        'form':form,
    }

    return render(
        request,
        'app/password_change.html',
        context)

def user_view(request, username):
     u = get_object_or_404(User, username=username)
     articles = Article.objects.filter(user = u)
     comments = Comment.objects.filter(user = u)


     context = {
         'user': u,
         'comments':comments,
         'articles':articles,
          }
    
     return render(
        request, 
        'app/user_page.html',
        context)


def articles(request):
    """ Renders the articles page """
    u = UserCheck(request)
    saved_art = Article.objects.filter(user = u, released = False) 
    released_art = Article.objects.filter(user = u, released = True) 
    not_verified = Article.objects.filter(verified = False)

    print(not_verified)

    context = {
            'saved':saved_art,
            'released':released_art,
            'not_verified':not_verified,
            'user':u,
        }

    return render(
        request,
        'app/articles.html',
        context)

def create_article_tag(request):
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
                overview = form.cleaned_data['overview'],
                verified = False,
                released = True,
                tag = True,
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
                overview = form.cleaned_data['overview'],
                verified = False,
                released = False,
                tag = True,
                )
            return redirect('articles')

    context = {
        'user':u,
        'form':form,
        }

    return render(
        request,
        'app/article_form_tag.html',
        context)

def create_article_html(request):
    u = UserCheck(request)
    form =  ArticleForm(request.POST or None, request.FILES or None)
    if 'CREATE' in request.POST:
        if form.is_valid():
            article.name = form.cleaned_data['name']
            article.engine = form.cleaned_data['engine']
            article.picture = form.cleaned_data['picture']
            article.text = form.cleaned_data['text']
            article.overview = form.cleaned_data['overview']
            article.released = True
            article.save()
            return redirect('articles')

    if 'SAVE' in request.POST:
        if form.is_valid():
            article.name = form.cleaned_data['name']
            article.engine = form.cleaned_data['engine']
            article.picture = form.cleaned_data['picture']
            article.text = form.cleaned_data['text']
            article.overview = form.cleaned_data['overview']
            article.released = false
            article.save()
            return redirect('articles')

    context = {
        'user':u,
        'form':form,
        }

    return render(
        request,
        'app/article_form_html.html',
        context)

def create_article_saved(request, article_id):
    u = UserCheck(request)

    article = get_object_or_404(Article, pk = article_id)

    article_data = {'name':article.name,
                    'engine':article.engine,
                    'picture':article.picture,
                    'text':article.text,
                    'overview':article.overview}

    if article.tag:
        form =  ArticleForm(request.POST or None, request.FILES or None, initial=article_data)
        if 'CREATE' in request.POST:
            if form.is_valid():
                article.name = form.cleaned_data['name']
                article.engine = form.cleaned_data['engine']
                article.picture = form.cleaned_data['picture']
                article.text = form.cleaned_data['text']
                article.overview = form.cleaned_data['overview']
                article.released = True
                article.save()
                return redirect('articles')

        if 'SAVE' in request.POST:
            if form.is_valid():
                article.name = form.cleaned_data['name']
                article.engine = form.cleaned_data['engine']
                article.picture = form.cleaned_data['picture']
                article.text = form.cleaned_data['text']
                article.overview = form.cleaned_data['overview']
                article.released = False
                article.save()
                return redirect('articles')

        context = {
            'user':u,
            'form':form,
            'article':article,
            }

        return render(
            request,
            'app/article_form_saved.html',
            context)
    else:
        form =  ArticleForm(request.POST or None, request.FILES or None)
        if 'CREATE' in request.POST:
            if form.is_valid():
                article.update(
                    user = u,
                    name = form.cleaned_data['name'],
                    engine = form.cleaned_data['engine'],
                    picture = form.cleaned_data['picture'],
                    text = form.cleaned_data['text'],
                    overview = form.cleaned_data['overview'],
                    verified = False,
                    released = True,
                    tag = True,
                    )
                return redirect('articles')

        if 'SAVE' in request.POST:
            if form.is_valid():
               article.update(
                    user = u,
                    name = form.cleaned_data['name'],
                    engine = form.cleaned_data['engine'],
                    picture = form.cleaned_data['picture'],
                    text = form.cleaned_data['text'],
                    overview = form.cleaned_data['overview'],
                    verified = False,
                    released = False,
                    tag = True,
                    )
            return redirect('articles')

        context = {
            'user':u,
            'form':form,
            'article':article,
            }

        return render(
            request,
            'app/article_form_saved.html',
            context)

def article_detail(request, article_id):
    u = UserCheck(request)

    template = loader.get_template('app/article.html')

    article = get_object_or_404(Article, pk=article_id)

    comments = Comment.objects.filter(article = article)

    subcomments = []

    for comment in comments:
        subcomments += SubComment.objects.filter(comment = comment)

    if article.tag:
        html = MakeHTML(article.text)
    else:
        html = article.text
    
    if request.method == "POST":
        if 'COMMENT' in request.POST:
            comment_form = CommentForm(request.POST)
            subcomment_form = SubCommentForm()
            if comment_form.is_valid():
                Comment.objects.create(
                    user = u,
                    article = article,
                    text = comment_form.cleaned_data["text"],
                    time = datetime.now(),
                    )
        if 'SUBCOMMENT' in request.POST:
            comment_form = ()
            subcomment_form = SubCommentForm(request.POST)
            if subcomment_form.is_valid():
                SubComment.objects.create(
                        user = u, 
                        comment = None,
                        text = subcomment_form.cleaned_data["text"],
                        time = datetime.now(),
                     )
    else:
        comment_form = CommentForm()
        subcomment_form = SubCommentForm()

    context = {
         'user':u,
         'article':article,
         'html':html,
         'comments': comments,
         'subcomments':subcomments,
         'comment_form':comment_form,
         'subcomment_form':subcomment_form,
         }

    return render(
         request,
         'app/article.html',
         context
         )

def verify_article(request, article_id):
     article = get_object_or_404(Article, pk = article_id)

     article.verified = True;
     article.save();

     return redirect('articles')
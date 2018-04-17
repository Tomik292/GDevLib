from django.contrib.auth.models import User
from .models import Article


def UserCheck(request):
    if request.user.is_authenticated:
        username = request.user
        return User.objects.get(username=username)
    else:
        return None

def MakeHTML(article_text):

    control_chars = dict.fromkeys(range(32))
    no_spaces = article_text.translate(control_chars)

    chars_array = no_spaces.split("|")

    no_zeros, html_dict = [], []
    html = ""

    for i in range(len(chars_array)):
        if(len(chars_array[i]) != 0 and chars_array[i] != " "):
            no_zeros.append(chars_array[i])

    for i in range(0,len(no_zeros)-1,2):
        html_dict.append({
                "tag": no_zeros[i],
                "value": no_zeros[i+1]
            })
    
    for val in html_dict:
        if val["tag"] == "p":
            html += "<p class='a_p'>" + val["value"] + "</p>"
        elif val["tag"] == "h1":
            html += "<h1 class='a_h1'>" + val["value"] + "</h1>"
        elif val["tag"] == "h2":
            html += "<h2 class='a_h2'>" + val["value"] + "</h2>"
        elif val["tag"] == "h3":
            html += "<h3 class='a_h3'>" + val["value"] + "</h3>"
        elif val["tag"] == "h4":
            html += "<h4 class='a_h4'>" + val["value"] + "</h4>"
        elif val["tag"] == "code":
            html += "<code class='a_code'>" + val["value"] + "</code>"
        elif val["tag"] == "a":
            url = val["value"].split("@")
            if len(url) > 1 : 
                html += "<a href='http://"+ url[1]+"' class='a_a' target='_blank'>" + url[0] + "</a>"
        elif val["tag"] == "img":
            html += "<img src='" + val["value"] + "'/>"
        else:
            html += ""
    return html

def filter_articles(words, game_engine):
    split_words = words.split(" ")  #rozdělení vstupu
    articles_id = [] #pole pro id uživatelů

    for key_word in split_words:
        articles = Article.objects.filter(text__icontains = key_word) #všechny články s daným slovem
        for article in articles:
            articles_id.append(article.id) #přidá id jednotlivých článků
    
    articles = Article.objects.filter(id__in = articles_id).filter(engine = game_engine).order_by('-points') 
    #filtr všech id v poli, s daným enginem, seřazeným podle hodnocení od největšího

    return articles


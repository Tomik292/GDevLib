from django.contrib.auth.models import User


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
        if(len(chars_array[i]) != 0):
            no_zeros.append(chars_array[i])
    

    for i in range(0,len(no_zeros)-1,2):
        html_dict.append({
                "tag": no_zeros[i],
                "value": no_zeros[i+1]
            })

    for val in html_dict:
        if val["tag"] == "p":
            html += "<p>" + val["value"] + "</p>"
        elif val["tag"] == "h1":
            html += "<h1>" + val["value"] + "</h1>"
        elif val["tag"] == "h2":
            html += "<h2>" + val["value"] + "</h2>"
        elif val["tag"] == "h3":
            html += "<h3>" + val["value"] + "</h3>"
        elif val["tag"] == "h4":
            html += "<h4>" + val["value"] + "</h4>"
        elif val["tag"] == "code":
            html += "<code>" + val["value"] + "</code>"
        elif val["tag"] == "a":
            html += "<a>" + val["value"] + "</a>"
        elif val["tag"] == "img":
            html += "<img src='" + val["value"] + "'/>"
        else:
            html += ""

    return html

ENGINE_CHOICES = (
    ("UNITY", "Unity Engine"),
    ("CRY", "Cry Engine"),
    ("UNREAL", "Unreal Engine"),
    ("OTHER", "Other Engines"),
)

from django.contrib.auth.models import User


def UserCheck(request):
    if request.user.is_authenticated:
        username = request.user
        return User.objects.get(username=username)
    else:
        return None

ENGINE_CHOICES = (
    ("UNITY", "Unity Engine"),
    ("CRY", "Cry Engine"),
    ("UNREAL", "Unreal Engine"),
    ("OTHER", "Other Engines"),
)

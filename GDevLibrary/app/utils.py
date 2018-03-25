from django.contrib.auth.models import User


def UserCheck(request):
    username = request.user if request.user.is_authenticated else None
    u = User.objects.get(username=username)
    return u

ENGINE_CHOICES = (
    ("UNITY", "Unity Engine"),
    ("CRY", "Cry Engine"),
    ("UNREAL", "Unreal Engine"),
    ("OTHER", "Other Engines"),
)

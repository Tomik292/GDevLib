from .models import Message, Category, UserExtension, Article, Comment, SubComment
from django.contrib import admin

admin.site.register(Message)
admin.site.register(Category)
admin.site.register(UserExtension)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(SubComment)
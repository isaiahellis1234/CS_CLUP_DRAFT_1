# blog/admin.py

from django.contrib import admin
from .models import Post, Comment

# Register the Post model to be accessible via Django Admin
admin.site.register(Post)
admin.site.register(Comment)

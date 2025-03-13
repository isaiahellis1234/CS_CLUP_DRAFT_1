# blog/admin.py

from django.contrib import admin
from .models import Post

# Register the Post model to be accessible via Django Admin
admin.site.register(Post)

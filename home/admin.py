from django.contrib import admin
# import Post from models.py class Post
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

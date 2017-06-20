from django.contrib import admin
from .models import Post
# Register your models here.

#models 의 post를 임포트해왔다!
admin.site.register(Post)
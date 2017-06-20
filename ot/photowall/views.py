from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request) :
    'DB에서 Post 목록을 가져와서 HTML 문자열을 생성/응답한다.'
    return render(request, 'photowall/index.html', {

      'post_list' : Post.objects.all(),

    })

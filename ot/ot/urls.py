"""ot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#추가
from django.conf import settings
from django.conf.urls.static import static

#불러오기
from photowall.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index), #row '^$' ^ 문자열 시작 $문자열 끝, 즉 최상위 주소 = localhost 일 시 index 함수
]

#추가
#urlpattern 항목 추가하기(리스트예요!)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
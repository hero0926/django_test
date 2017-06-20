from django.db import models
from django.utils import timezone

#blog post설정

class Post(models.Model):

	#다른 모델 링크
    author = models.ForeignKey('auth.User')
    
    #글자수가 제한된 텍스트
    title = models.CharField(max_length=200)
    
    #글자수 무제한 텍스트
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __어쩌구__ dunder 더블 언더스코어

    def __str__(self):
        return self.title
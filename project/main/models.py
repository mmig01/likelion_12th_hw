from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    #유저를 외래키로 가짐 -> Post 데이터베이스에는 user 의 id 정보가 추가
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    feel = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:20]
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    #user은 Django에서 제공해주는 model,즉 writer는 user을 참조한다. 이 user는 무결성 참조조건에 의해 존재하는 값 혹은 null 값 만 써야한다
    #참조하는 user가 삭제될 때 게시글을 남기거나 삭제하는 옵션 = on_delete, CASCADE = 삭제
    like = models.ManyToManyField(User , related_name="likes", blank=True)






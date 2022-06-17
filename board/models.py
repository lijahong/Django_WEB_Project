from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField()
    contents = models.TextField()
    create_date=models.DateTimeField(auto_now_add = True)



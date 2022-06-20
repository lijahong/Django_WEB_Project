from django.db import models

class Reply(models.Model):
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
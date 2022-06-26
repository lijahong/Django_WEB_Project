from django.contrib.auth.models import AbstractUser #model만 수정, 기능은 가져와서 쓴다
from django.db import models

class User(AbstractUser) :
    pass


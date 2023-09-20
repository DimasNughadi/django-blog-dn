from django.db import models
from datetime import datetime
today = datetime.now()
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = today.strftime('%Y.%m.%d')

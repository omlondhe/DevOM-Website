from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models

# Create your models here.


class PlayStore(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=251)
    description = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=521)
    link = models.CharField(max_length=521)
    imageURL = models.CharField(max_length=521)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title


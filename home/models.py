from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=251)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.sno) + '. ' + self.name + ' - ' + self.email


class Donate(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=251)
    last_name = models.CharField(max_length=251)
    email = models.EmailField()
    amount = models.CharField(max_length=11)
    description = models.TextField()

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name

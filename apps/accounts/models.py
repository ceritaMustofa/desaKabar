from django.db import models

# Create your models here.

class Accounts(models.Model):
    username = first_name= models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=False, blank=False)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    def __str__(self):
        return self.username, self.email

from django.db import models
from django.forms import ModelForm

# Create your models here.

class NewUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

# Create your forms here.

class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ['name', 'email']
    
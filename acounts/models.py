from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    texto = models.TextField(max_length=300,null=True)
    DataNasci = models.DateField(null=True)
    imagem = models.ImageField(upload_to='media/', blank = True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
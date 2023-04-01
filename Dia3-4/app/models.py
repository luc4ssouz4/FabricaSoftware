from django.db import models

class ToDo(models.Model):
    atividade = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
from django.db import models

class Cheque_Palavra(models.Model):
    palavra = models.CharField(max_length=200)

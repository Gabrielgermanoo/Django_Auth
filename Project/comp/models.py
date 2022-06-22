from pyexpat import model
from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=50, unique= True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "Users"

    def __str__(self) -> str:
        return self.login


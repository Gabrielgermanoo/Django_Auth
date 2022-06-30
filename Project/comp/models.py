from pyexpat import model
from django.db import models

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "Login"

    def __str__(self) -> str:
        return self.login


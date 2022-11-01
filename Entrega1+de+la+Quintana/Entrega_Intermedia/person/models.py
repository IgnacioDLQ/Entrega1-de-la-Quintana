from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    birth_date = models.DateField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.last_name}"
from django.db import models

class Bank(models.Model):
    entity = models.CharField(max_length=40)

    def __str__(self):
        return {self.entity}
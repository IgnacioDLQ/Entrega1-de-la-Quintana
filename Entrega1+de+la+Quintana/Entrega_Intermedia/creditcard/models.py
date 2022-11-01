from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField


class CreditCard(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    code = models.IntegerField(null=False, blank=False)
    expire_date = RichTextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "name",
            "code",
            "expire_date"
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Credit Card: {self.name} | code: {self.code} | expire_date: {self.expire_date}"
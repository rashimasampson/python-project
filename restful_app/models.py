from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title must be at least 2 characters long."
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters long."
        if len(postData['description']) < 10:
            errors["description"] = "Description must be at least 10 characters long."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.CharField(max_length=25)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('name', 'subject')

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
# Note: Data fields are not encrypted as they are non-sensitive.
# Encryption (e.g., using django-fernet-fields) can be applied if storing PII.

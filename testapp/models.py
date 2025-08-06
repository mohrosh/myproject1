from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=250)
    short_description = models.TextField()
    document = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

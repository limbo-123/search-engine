from django.db import models
import uuid

class submit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=10000, null=True)
    description = models.CharField(max_length=2000000)
    date = models.DateField(auto_now_add=True, null=True)
    total_links = models.CharField(null=True, max_length=100000)
    meta = models.CharField(max_length=10000, null=True)
    def __str__(self):
        return self.title

class url(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    url = models.CharField(max_length=10000)
    date = models.DateField(auto_created=True, null=True)
    links = models.CharField(max_length=10000, null=True)
    def __str__(self):
        return self.url

    


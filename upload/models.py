from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    scripture = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    audio = models.FileField()
    slides = models.FileField()
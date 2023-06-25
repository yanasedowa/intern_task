from django.db import models


class TextRequest(models.Model):
    text = models.TextField()

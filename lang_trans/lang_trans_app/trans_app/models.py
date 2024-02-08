from django.db import models

class Translation(models.Model):
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    text_to_translate = models.TextField()
    translated_text = models.TextField(blank=True, null=True)
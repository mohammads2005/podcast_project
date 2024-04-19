from django.db import models

from base_model.base_model import BaseModel

# Create your models here.


class Episode(BaseModel):
    title = models.TextField(verbose_name="Episode Title")
    audio_file = models.FileField(upload_to="audios/", verbose_name="Audio Content")

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ['created_date']

    def __str__(self):
        return self.title

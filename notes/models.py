from django.db import models
from django.conf import settings


class Note(models.Model):
    """
    Model for storing users notes
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='note')
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = "заметка"
        verbose_name_plural = 'заметки'
        ordering = ["-created"]

    def _str_(self):
        return self.user.username + self.title

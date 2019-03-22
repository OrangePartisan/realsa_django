from django.db import models
from django.utils.timezone import now

# Create your models here.
class RealsaBlog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Realsa blog"
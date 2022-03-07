from django.db import models


class ScanImage(models.Model):

    image_url = models.ImageField(upload_to='images/', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    stress_level = models.FloatField(default=None, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Scan Images'
        ordering = ['-id']

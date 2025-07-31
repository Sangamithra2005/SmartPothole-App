from django.db import models

class PotholeReport(models.Model):
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='potholes/', blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location

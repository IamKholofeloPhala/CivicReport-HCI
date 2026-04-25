from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('Pothole', 'Hazardous Pothole'),
        ('Water', 'Major Pipe Burst'),
        ('Power', 'Grid Failure'),
        ('Traffic', 'Traffic Light Malfunction'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending') # Pending, Dispatched, Resolved
    created_at = models.DateTimeField(auto_now_add=True)

    def __cl__(self):
        return f"{self.category} at {self.location}"
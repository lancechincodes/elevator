from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (

)
class Application(models.Model):
    IN_PROGRESS = 'IP'
    APPLIED = 'A'
    INTERVIEWED = 'I'
    OFFERED = 'O'
    REJECTED = 'R'
    STATUS_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (APPLIED, 'Applied'),
        (INTERVIEWED, 'Interviewed'),
        (OFFERED, 'Offered'),
        (REJECTED, 'Rejected')
    ]

    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    application_url = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    # foreign key linking to user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=IN_PROGRESS,)
    date_submitted = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.company} - {self.position}'
    
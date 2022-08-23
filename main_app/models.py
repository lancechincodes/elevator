from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
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
class Application(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    application_link = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, 
        choices=STATUS_CHOICES, 
        default=STATUS_CHOICES[0][0],
    )
    date_applied = models.DateField('date applied')
    notes = models.TextField(max_length=500)
    # foreign key linking to user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} applied to {self.company} as a {self.position}'

    # reverse will return the correct path for the detail named route
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
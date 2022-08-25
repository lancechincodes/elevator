from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
INCOMPLETE = 'IC'
APPLIED = 'A'
INTERVIEWED = 'I'
OFFERED = 'O'
REJECTED = 'R'
STATUS_CHOICES = [
    (INCOMPLETE, 'Incomplete'),
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
        max_length=2, # corresponds to 1st index of sets of tuples
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0], 
    )
    date_applied = models.DateField('date applied', null=True, blank=True) # parameter customizes what is shown in forms
    notes = models.TextField(max_length=500, blank=True)
    # foreign key linking to user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete will delete all children of deleted parent element

    # dunder (double underscore) method to print a useful message
    def __str__(self):
        return f'{self.user.username} created an entry for {self.company} as a {self.position}'

    # reverse will return the correct path named application index
    def get_absolute_url(self):
         return reverse('applications_index')

    # order desc by date
    class Meta:
        ordering = ['-date_applied']
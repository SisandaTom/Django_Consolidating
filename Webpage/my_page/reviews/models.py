from django.db import models
# Create your models here.

# definig class Reviews to write syudent reviews for the website
class Reviews(models.Model):
# Default behaviour - Django creates primary keys for you
# taking title, bosy and the student's name as input
    title = models.CharField(max_length=140)
    body = models.TextField()
    name = models.CharField(max_length=140)
def __str__(self):
    return self.title

from django.db import models
# Create your models here.


class Reviews(models.Model):
    """
    Model representing student reviews for the website.

    This model stores information about student reviews, including the title,
    body, and the student's name.

    Attributes:
        title (str): The title of the review (max length: 140 characters).
        body (str): The main content of the review.
        name (str): The name of the student who wrote the review (max length: 140 characters).

    Methods:
        __str__(): Returns the title of the review as its string representation.

    Usage:
        You can use this model to store and retrieve student reviews for your website.
    """

    title = models.CharField(max_length=140)
    body = models.TextField()
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.title

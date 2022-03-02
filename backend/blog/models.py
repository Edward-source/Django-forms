from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    state = models.CharField(null=False, max_length=30)
    company = models.CharField(max_length=30)
    date_posted = models.DateField(auto_now=True)
    closing_date = models.DateField()
    Job_description = models.TextField()

    def __str__(self,):
        return self.position
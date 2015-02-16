from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self): #__unicode__ rather than __str__ in python 2.7
        return self.title 

class ListItem(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    amount = models.DecimalField(max_digits=3, decimal_places=1)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    recurring = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self): #__unicode__ rather then __str__ in python 2.7
        return self.name 
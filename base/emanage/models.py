from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue Name',max_length=180)
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Event Name',max_length=200)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey('Venue', blank=True, null=False, on_delete=models.CASCADE)
    manager = models.CharField(max_length=120)

    def __str__(self):
        return self.name
from django.db import models

class bulletJournal(models.Model):
    title= models.CharField(max_length=100)
    complated= models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title()
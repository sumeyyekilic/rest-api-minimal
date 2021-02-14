from django.db import models

class BulletJournal(models.Model):
    title= models.CharField(max_length=300)
    complated= models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title()
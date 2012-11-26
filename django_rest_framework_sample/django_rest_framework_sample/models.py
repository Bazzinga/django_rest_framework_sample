from django.db import models
    
class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    adress = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 50)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username
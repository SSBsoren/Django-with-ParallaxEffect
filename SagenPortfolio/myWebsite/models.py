from django.db import models

# Create your models here.
class MyWebsite(models.Model):
    complete = models.BooleanField(default = False)
    webtext = models.CharField(max_length = 50)

    def __str__(self):
        return self.webtext

from django.db import models

class Movie(models.Model):
    filmtitle = models.CharField(max_length=60, null=False)
    filmgenre = models.CharField(max_length=30, null=False)
    filmdirector = models.CharField(max_length=60, null=False)
    filmpublicationyear = models.IntegerField(null=False)
    synopsisofthefilm = models.TextField(null=False)
    
    def __str__(self) -> str:
        return self.filmtitle
    
    

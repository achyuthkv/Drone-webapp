from django.db import models

class VictimDetails(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    phoneno = models.IntegerField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'VictimDetails'
        verbose_name_plural = 'VictimDetails' 
from django.db import models


class Trainning(models.Model):
    site = models.URLField()
    content = models.TextField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.site

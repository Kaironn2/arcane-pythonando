from django.db import models


class Trainning(models.Model):
    site = models.URLField()
    content = models.TextField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.site


class TrainningData(models.Model):
    metadata = models.JSONField(null=True, blank=True)
    text = models.TextField()


class Question(models.Model):
    trainning_data = models.ManyToManyField(TrainningData)
    question = models.TextField()

    def __str__(self):
        return self.question

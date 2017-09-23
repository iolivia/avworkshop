from django.db import models

# Movie object
class Movie(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()

    @classmethod
    def create(cls, title, image_url):

        instance = cls(
            title=title, 
            image_url=image_url)

        return instance
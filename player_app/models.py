from django.db import models

# Movie object
class Movie(models.Model):
    imdb_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    year = models.CharField(max_length=4)
    plot_outline = models.CharField(max_length=200)
    rating = models.FloatField()
    trailer_url = models.URLField()

    @classmethod
    def create(cls, 
        imdb_id, 
        title, 
        image_url, 
        year=None, 
        plot_outline=None,
        trailer_url=None):

        instance = cls(
            imdb_id=imdb_id,
            title=title, 
            image_url=image_url,
            year=year,
            plot_outline=plot_outline,
            trailer_url=trailer_url)

        return instance
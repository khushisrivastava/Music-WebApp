from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image = models.CharField(max_length=255, blank=True)
    singer = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.name

class Playlist(models.Model):
    song = models.ManyToManyField(Song, blank=True)
    name = models.CharField(max_length=255, blank=False)
    VIEW_CHOICE = (
        ("private", "Private"),
        ("public", "Public"),
        ("follower", "Followers-only")
    )
    visiblity = models.CharField(choices=VIEW_CHOICE, default=None, max_length=10)

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.name

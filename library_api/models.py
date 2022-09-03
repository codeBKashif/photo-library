from django.db import models

from library_api.types import PhotoDestinations, PhotoFormats

class Photo(models.Model):

    class Formats(models.TextChoices):
        PDF = PhotoFormats.PDF.value
        JSON = PhotoFormats.JSON.value
        XML = PhotoFormats.XML.value

    class Destinations(models.TextChoices):
        LOCAL_DRIVE = PhotoDestinations.LOCAL_DRIVE.value
        FTP = PhotoDestinations.FTP.value
        S3 = PhotoDestinations.S3.value

    name = models.TextField()
    formats = models.CharField(choices=Formats.choices, max_length=256)
    destinations = models.CharField(choices=Destinations.choices, max_length=256)
    time_added = models.DateTimeField(auto_now_add=True)

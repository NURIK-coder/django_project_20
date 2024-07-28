from django.core.validators import FileExtensionValidator
from django.db import models as m

# Create your models here.


class Video(m.Model):
    name = m.CharField('Name', max_length=30)
    datetime = m.DateField('Datetime', auto_now_add=True)
    img = m.FileField('File', upload_to='videos', blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['mp4'])

    ])
    created_at = m.DateTimeField('Created at', auto_now_add=True)


    def __str__(self):
        return self.name
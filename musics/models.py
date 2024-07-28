from django.core.validators import FileExtensionValidator
from django.db import models as m

# Create your models here.

class Music(m.Model):
    name = m.CharField('Name', max_length=30)
    year = m.IntegerField('Year')
    file = m.FileField('File', upload_to='musics', blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['mp3'])

    ])
    created_at = m.DateTimeField('Created at', auto_now_add=True)


    def __str__(self):
        return self.name


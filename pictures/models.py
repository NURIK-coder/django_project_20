from django.core.validators import FileExtensionValidator
from django.db import models as m

# Create your models here.

class Picture(m.Model):
    name = m.CharField('Name', max_length=20)
    img = m.ImageField('Image', upload_to='imgaes', blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png'])

    ])

    def __str__(self):
        return self.name


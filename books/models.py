from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import FileExtensionValidator
from django.db import models as m


# Create your models here.


class Book(m.Model):
    name = m.CharField('Name', max_length=50, default='Poco\'s adventures')
    description = m.TextField('Description', default='good book!')
    num_page = m.IntegerField('Num pages', default=121)
    author = m.CharField('Author', max_length=30, default='Abdulla Qodriy')
    file = m.FileField('File', upload_to='books', blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['doc', 'pdf'])

    ])

    def __str__(self):
        return self.name


class FavouriteItem(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    content_type = m.ForeignKey('contenttypes.ContentType', on_delete=m.CASCADE)
    object_id = m.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.user} - {self.content_object}"

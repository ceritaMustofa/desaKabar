from io import BytesIO
from django.core.files import File
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

# Create your models here.
class Aparatur(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    
    def __str__(self):
        return self.title

class Aparat(models.Model):
    position = models.ForeignKey(Aparatur, on_delete=models.CASCADE, related_name='kepaladesas')
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    reign = models.CharField(max_length=225)
    address = models.CharField(max_length=1024)
    biography = RichTextUploadingField()
    status = models.BooleanField(default=False)

    thumbnail= models.ImageField(upload_to='uploads/', blank=True, null=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.thumbnail)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail



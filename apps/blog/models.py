from io import BytesIO
from django.core.files import File
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = RichTextUploadingField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail= models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

class CategoryPostDesa(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

class PostDesa(models.Model):
    category = models.ForeignKey(CategoryPostDesa, on_delete=models.CASCADE, related_name='postDesas')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = RichTextUploadingField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail= models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size =(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

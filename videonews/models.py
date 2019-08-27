from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.

CATEGORIES = [
    ('Health','health'),
    ('Skills','skills'),
    ('Sports','sports'),
    ('Politics','politics'),
    ('Social','social'),
    ('Motivateion','motivation'),
    ('Business','business')
]


class ContactUs(models.Model):
    email = models.EmailField()
    message = models.TextField()


class News(models.Model):
    title = models.CharField(max_length=100)
    categories = models.CharField(choices=CATEGORIES, default='Education', max_length=40)
    image = models.ImageField(upload_to='profile_pics')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.categories


class Video(models.Model):
    title = models.CharField(max_length=100)
    categories = models.CharField(choices=CATEGORIES, default='Education', max_length=40)
    content = models.FileField("content", upload_to='profile_pics', max_length=100)
    date = models.DateTimeField(default=timezone.now)
    #['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    comments = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
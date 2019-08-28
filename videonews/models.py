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
    
# class LNMOnline(models.Model):
#     CheckOutRequestID = models.CharField(max_length=50, blank=True, null=True)
#     MerchantRequestID = models.CharField(max_length=20, blank=True, null=True)
#     Result_code =models.IntegerField(blank=True, null=True)
#     ResultDesc = models.CharField(max_length=120, blank=True, null=True)
#     Amount = models.FloatField(blank=True, null=True)
#     MpesaReceiptNumber = models.CharField(max_length=15, blank=True, null=True)
#     Balance = models.CharField(max_length=12, blank=True, null=True)
#     Transaction_date = models.DateTimeField(blank=True, null=True)
#     Phone_number = models.CharField(max_length=13, blank=True, null=True)

#     def __str__(self):
#         return f'{self.Phone_number} has sent {self.Amount} >> {self.MpesaReceiptNumber}'

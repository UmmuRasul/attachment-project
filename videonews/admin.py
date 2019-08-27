from django.contrib import admin
from models import Post, Video, News, ContactUs

# Register your models here.
admin.site.register(Post)
admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Video)
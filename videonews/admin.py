from django.contrib import admin
from .models import Post, Video, News, ContactUs

# Register your models here.
admin.site.register(Post)
admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Video)





# class LNMOnlineAdmin(admin.ModelAdmin):
#     list_display = ('Phone_number', 'MpesaReceiptNumber', 'Amount', 'Transaction_date')

# admin.site.register(LNMOnline, LNMOnlineAdmin)

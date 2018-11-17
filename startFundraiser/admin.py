from django.contrib import admin

# Register your models here.

from .models import Campaign, FAQs, Update, Post

admin.site.register(Campaign)
admin.site.register(FAQs)
admin.site.register(Update)
admin.site.register(Post)

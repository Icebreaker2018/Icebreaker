from django.contrib import admin

# Register your models here.

from .models import Campaign, FAQs, Update

admin.site.register(Campaign)
admin.site.register(FAQs)
admin.site.register(Update)

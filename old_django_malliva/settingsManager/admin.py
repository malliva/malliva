from django.contrib import admin
from .models import SocialMediaPage, Configuration, TemplateStyling

# Register your models here.
admin.site.register(SocialMediaPage)
admin.site.register(TemplateStyling)
admin.site.register(Configuration)

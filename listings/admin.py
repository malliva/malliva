from django.contrib import admin
from .models import Listing, ListingImage

# Register your models here.

admin.site.register(Listing)
admin.site.register(ListingImage)

from django.contrib import admin
from .models import MarketplaceAccount, Plan, Subscription

# Register your models here.

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(MarketplaceAccount)

from django.contrib import admin
from .models import Client, Theme, Item, Rent

admin.site.register(Client)
admin.site.register(Theme)
admin.site.register(Item)
admin.site.register(Rent)
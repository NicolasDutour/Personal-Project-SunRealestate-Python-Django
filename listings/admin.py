from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'realtor')
    list_display_links = ('title',)
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'postcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

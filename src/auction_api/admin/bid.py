from django.contrib import admin


class BidModelAdmin(admin.ModelAdmin):
    list_display = ("auction", "user", "price")

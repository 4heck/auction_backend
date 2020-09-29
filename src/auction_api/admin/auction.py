from django.contrib import admin


class AuctionModelAdmin(admin.ModelAdmin):
    list_display = ("title", "get_is_active")

    def get_is_active(self, obj):
        return obj.is_active

    get_is_active.boolean = True

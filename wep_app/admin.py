from django.contrib import admin
from wep_app.models import *
# Register your models here.

admin.site.register(Cart)
admin.site.register(Orderby)
admin.site.register(user)
admin.site.register(Wishlist)

class addedexradatas(admin.StackedInline):
    model = Cart

class Prodects(admin.ModelAdmin):
    list_display = ('name', 'model', 'category', 'brand', 'price', 'stock')
    list_display_links = ('name', 'model', 'category', 'brand','stock')
    search_fields = ('name', 'model', 'category', 'brand', 'price', 'stock')
    list_editable = ('price', )
    inlines = [addedexradatas]
    list_filter = ('brand', 'price', 'stock')

admin.site.register(Prodect, Prodects)



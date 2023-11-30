from django.contrib import admin
from . import models


class InformationAdmin(admin.StackedInline):
    model = models.Information




@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','price', 'discount','discounted_price')
    list_filter = ('category',)
    search_fields = ('title',)
    inlines = (InformationAdmin,)




admin.site.register(models.CategoryBook)
admin.site.register(models.Author)
admin.site.register(models.Subject)
admin.site.register(models.Publisher)
admin.site.register(models.PrintYear)

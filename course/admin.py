from django.contrib import admin
from . import models

# Register your models here.

class CommentIline(admin.StackedInline):
    model = models.Comment

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('__str__','views', 'title', 'status','slug','show_image')
    list_editable = ('title',)
    list_filter = ('status',)
    search_fields = ('title', 'body')
    inlines = (CommentIline,)

@admin.register(models.CategoryCourse)
class CtegoryCourseAdmin(admin.ModelAdmin):
    list_display = ('title',)


# @admin.register(models.Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user',)

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('__str__','course')


# admin.site.register(models.Like)

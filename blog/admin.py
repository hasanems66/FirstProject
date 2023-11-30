from django.contrib import admin
from django import forms

from . import models
from .models import Article


class Article_CommentIline(admin.StackedInline):
    model = models.Article_Comment


# custom filter
class FilterByTitle(admin.SimpleListFilter):
    title = ' کلید های پر تکرار'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('django', 'جنگو'),
            ('python', 'پایتون'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','slug', 'status','show_image' )
    list_editable = ('title',)
    list_filter = ('status', FilterByTitle)
    search_fields = ('title', 'body')
    inlines = (Article_CommentIline,)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ['title', ]}


@admin.register(models.ArticleLike)
class ArticleLikeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'article')


# class ArticleAdminForm(forms.ModelForm):
#     # content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Article
#         fields = '__all__'


# class ArticleAdmin(admin.ModelAdmin):
#     form = ArticleAdminForm
#     list_display = ('__str__', 'title', 'slug', 'status', 'show_image')
#     list_editable = ('title',)
#     list_filter = ('status', FilterByTitle)
#     search_fields = ('title', 'body')
#     inlines = (Article_CommentIline,)
#
#
# admin.site.register(Article, ArticleAdmin)

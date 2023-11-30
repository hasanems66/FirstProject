from django.urls import path,re_path
from . import views



app_name = 'blog'

urlpatterns = [
    # path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    re_path(r'detail/(?P<slug>[-\w]+)', views.ArticleDetailView.as_view(), name='article_detail'),
    path('list', views.ArticleListView.as_view(), name='article_list'),
    path('search_blog/', views.search_blog, name='search_blog'),
    # path('test/<slug:slug>/<int:pk>', views.article_like, name='blog_like'),

    re_path(r"test/(?P<slug>[-\w]+)/(?P<pk>[-\w])", views.article_like, name='blog_like'),
    # path('category/blog/<str:title>', views.category_detail_blog, name='blog_category'),

    re_path(r'category/blog/(?P<slug>[-\w]+)', views.category_detail_blog, name='blog_category'),
    # path(r'category/blog/<int:id>', views.category_detail_blog, name='blog_category'),


    # path('art_list', views.articles_list, name= 'article_list')
]
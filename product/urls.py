from django.urls import path,re_path
from . import views


app_name = 'product'
urlpatterns = [
    re_path(r"detail/(?P<slug>[-\w]+)", views.BookDetailView.as_view(),name='book_detail'),
    path('book/list', views.BookListView.as_view(), name= 'book_list'),
    path('category/book/<str:title>', views.category_detail_book, name='book_categories'),

]
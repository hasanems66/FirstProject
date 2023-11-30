from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,render
from django.views.generic import DetailView,ListView

from product.models import Book,CategoryBook




def book_detail(request,title):
    book = get_object_or_404(Book, title=title)
    return render(request, 'product/book_detail.html', context={'book':book})



class BookDetailView(DetailView):
    model = Book





class BookListView(ListView):
    model = Book



def category_detail_book(request, title):
    category=get_object_or_404(CategoryBook, title=title)
    books = category.books.all()
    page_number = request.GET.get('page')
    # print(page_number)
    paginator = Paginator(books, 18)
    object_list = paginator.get_page(page_number)

    return render(request, 'product/book_list.html', context={'object_list':object_list})




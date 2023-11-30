from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView
from course.models import Course
from blog.models import Article
from product.models import Book







def home(request):
    courses = Course.objects.filter(status=True)[:4]
    articles = Article.objects.filter(status=True)[:3]
    books = Book.objects.all()[:12]

    return render(request,'home/index.html', context={'courses': courses, 'articles': articles, 'books':books})
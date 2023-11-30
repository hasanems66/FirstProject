from course.models import Course,CategoryCourse
from blog.models import Article, Category
from product.models import CategoryBook
from footer.models import Footer


def recent_courses(request):
    recent_courses = Course.objects.all().order_by('-updated',)[:3]

    return {'recent_courses': recent_courses}



def recent_blog(request):
    recent_articles = Article.objects.order_by('-updated',)[:3]
    categorys = Category.objects.all()

    return {'recent_articles': recent_articles, 'categorys': categorys}


def category_book(request):
    category_book= CategoryBook.objects.all()
    return {'category_book':category_book}

def footer(request):
    footer = Footer.objects.all().last()
    return {'footer':footer}

def category_course(request):
    category_course= CategoryCourse.objects.all()
    return {'category_course':category_course}

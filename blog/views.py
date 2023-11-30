from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Article,Article_Comment, ArticleLike,Category
from django.views.generic import DetailView,ListView
from .mixins import CustomLoginRequireMixin







class ArticleDetailView(CustomLoginRequireMixin,DetailView):

    model = Article


    def post(self,request,slug,):
        article = get_object_or_404(Article, slug=slug)
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Article_Comment.objects.create(article=article, body=body, user_id=self.request.user.id, parent_id=parent_id)
        return redirect('blog:article_detail' , article.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.article_likes.filter(article__slug=self.object.slug, user_id= self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context



    def get(self,request,*args,**kwargs):
        article_slug = kwargs['slug']
        article = get_object_or_404(Article, slug=article_slug)
        article.views += 1
        article.save()
        return render(request, 'blog/article_detail.html', context={'article':article})


def article_like(request, slug,pk):
    print('hi')
    try:
        like = ArticleLike.objects.get(article__slug=slug, user_id= request.user.id)
        like.delete()
        return JsonResponse({'response': 'unliked'})

    except:
        ArticleLike.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})




# def testone(request):
#     print('hello codeyad')
#     return JsonResponse({'response': 'liked'})




def search_blog(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    # print(page_number)
    paginator=Paginator(articles,6)
    object_list = paginator.get_page(page_number)

    return render(request, 'blog/article_list.html', context={'page_obj':object_list})


class ArticleListView(ListView):
    model = Article
    # queryset = Article.objects.all()
    paginate_by = 12



# def category_detail_blog(request,title):
#     category = get_object_or_404(Category, title=title)
#     articles = category.articles.all()
#     page_number = request.GET.get('page')
#     paginator = Paginator(articles, 12)
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'blog/article_list.html', context={'page_obj':page_obj})


def category_detail_blog(request,slug):
    category = get_object_or_404(Category, slug=slug)
    # print(category)
    articles = category.articles.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 12)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/article_list.html', context={'page_obj':page_obj})






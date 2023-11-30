from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView, CreateView, FormView
from course.models import Course, Comment, Like,CategoryCourse
from django.core.paginator import Paginator


# function base

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, course=course, user=request.user, parent_id=parent_id)

    return render(request, 'course/course_detail.html', context={'course': course})



def course_list(request):
    courses = Course.objects.all()
    page_number = request.GET.get('page')
    # print(page_number)
    paginator = Paginator(courses, 12)
    object_list = paginator.get_page(page_number)
    return render(request, 'course/course_list.html', context={'courses': object_list})


def category_course_detail(request, title):
    category = get_object_or_404(CategoryCourse, title=title)
    courses = category.courses.all()
    page_number = request.GET.get('page')
    paginator = Paginator(courses, 12)
    object_list = paginator.get_page(page_number)
    return render(request, 'course/course_list.html', context={'courses': object_list})


def search(request):
    q = request.GET.get('q')
    courses = Course.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(courses, 6)
    object_list = paginator.get_page(page_number)
    return render(request, 'course/course_list.html', context={'courses': object_list})



def like(request, slug, pk):
    try:
        like = Like.objects.get(course__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({'response':'unliked'})
    except:
        Like.objects.create(course_id=pk, user_id=request.user.id)
        return JsonResponse({'response':'liked'})




# def test_like(request):
#     print('hello codeyad')
#     return JsonResponse({'response': 'hasan'})



# class base

class CourseDetailView(DetailView):
    model = Course
    # pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.likes.filter(course__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True

        else:
            context['is_liked'] = False
        return context

    def post(self,request, slug):
        course = get_object_or_404(Course, slug=slug)
        body = self.request.POST.get('body')
        parent_id = self.request.POST.get('parent_id')
        Comment.objects.create(body=body,course=course ,parent_id=parent_id, user_id=self.request.user.id)
        return redirect('course:course_details', course.slug)


    def get(self,request,*args,**kwargs):
        course_slug = kwargs['slug']
        course = get_object_or_404(Course, slug= course_slug)
        course.views += 1
        course.save()
        return render(request, 'course/course_detail.html', context={'course':course})









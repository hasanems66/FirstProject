from django.urls import path,re_path
from . import views



app_name = 'course'
urlpatterns = [
    # path('details/<int:pk>', views.course_detail, name='course_details'),
    # path('details/<slug:slug>', views.course_detail, name='course_details'),
    path('list', views.course_list, name='course_list'),
    path('search', views.search, name='search_courses'),
    # path('like/<slug:slug>/<int:pk>', views.like, name='course_like'),
    re_path(r"like/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)", views.like, name='course_like'),
    # path('test', views.test_like, name='test'),


    # path('details/<int:pk>', views.CourseDetailsView.as_view(), name='course_details'),
    # path('details/<slug:slug>', views.CourseDetailView.as_view(), name='course_details'),
    re_path(r"details/(?P<slug>[-\w]+)", views.CourseDetailView.as_view(), name='course_details'),
    path('category/detail/<str:title>', views.category_course_detail, name='course_category'),

]
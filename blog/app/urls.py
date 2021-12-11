from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('api/blog', views.blog_list.as_view()),
    path('api/blog/<int:pk>', views.blog_detail.as_view()),
    path('api/blog/user/<int:pk>', views.User_Blog.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

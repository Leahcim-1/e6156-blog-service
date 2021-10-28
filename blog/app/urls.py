from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('blog/', views.blog_list.as_view()),
    path('blog/<int:pk>', views.blog_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

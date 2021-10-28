from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('test/', views.test_list.as_view()),
    path('test/<int:pk>', views.test_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

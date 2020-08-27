from django.urls import path

# точка означает, что мы импортируем из текущей дериктории весь файл views
from . import views

urlpatterns = [
    path('post/<slug:post_name>/', views.PostView.as_view(), name='post'),
    path('category/<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view()),
]
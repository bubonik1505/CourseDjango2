from django.urls import path

# точка означает, что мы импортируем из текущей дериктории весь файл views
from . import views

urlpatterns = [
    path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post"),
    path("<slug:category_name>/", views.CategoryView.as_view(), name="category"),
    path("", views.HomeView.as_view()),
]
from django.urls import path

from . import views


urlpatterns = [
    path('add/', views.AddCategoryView.as_view()),
    path('list/', views.ListCategorView.as_view()),
    path('delete/<str:title>', views.DeleteCategoryView.as_view()),
]

from django.urls import path

from . import views


urlpatterns = [
    path('add/', views.AddAuthorView.as_view()),
    path('list/', views.ListAuthorView.as_view()),
    path('delete/<str:name>', views.DeleteAuthorView.as_view())
]

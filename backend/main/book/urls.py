from django.urls import path

from . import views


urlpatterns = [
    path('add/', views.AddBookView.as_view()),
    path('set/<int:isbn>', views.SetBookView.as_view()),

    # New
    path('get/<int:isbn>', views.GetBookView.as_view()),
    # New

    path('list/', views.ListBookView.as_view()),
    path('delete/<int:isbn>', views.DeleteBookView.as_view()),


    path('check/<int:isbn>', views.CheckBookView.as_view()),
]

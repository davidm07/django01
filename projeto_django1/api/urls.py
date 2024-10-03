from . import views
from django.urls import path


urlpatterns = [
    path('livros/', views.getLivros),
    path('livros/<int:pk>/', views.LivrosById)
]

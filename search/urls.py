from django.urls import path
from . import views
urlpatterns = [
    path('search/', views.SearchPage, name='search'),
    path('search-results/', views.results, name='search-results'),
]
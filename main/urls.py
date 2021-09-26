from django.urls import path
from .views import index, filter_methods, about

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('filter_methods', filter_methods, name='filter_methods'),
]

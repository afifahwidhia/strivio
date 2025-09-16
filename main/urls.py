from django.urls import path
from main.views import show_main, create_product, show_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('<int:id>/', show_product, name='show_product'),
]
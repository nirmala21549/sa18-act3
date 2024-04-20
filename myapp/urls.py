from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Root URL pattern
    path('<int:pk>/', views.show, name='show'),         # URL pattern for individual product details
    # Add more URL patterns here as needed
]

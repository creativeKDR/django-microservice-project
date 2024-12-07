
from django.urls import path
from . import views

urlpatterns = [
    path('product', views.get_products, name="product"),
    path('product/<int:pk>/', views.product_detail, name="details"),
]

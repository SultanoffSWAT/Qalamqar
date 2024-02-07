from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductsListAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductsDetailAPIView.as_view()),

]
from django.urls import path
from . import views

urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('<int:id>/', views.product_details, name='product_detail'),
	path('<int:id>/edit/', views.product_edit, name='edit_product'),
	path('<int:id>/delete/', views.delete_product, name='delete_product'),
]

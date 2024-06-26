from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('outfits/', views.all_outfits, name='outfits'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/product/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('outfit/add/', views.add_outfit, name='add_outfit'),
    path('outfit/delete/<int:outfit_id>/',
         views.delete_outfit, name='delete_outfit'),
    path('outfit/edit/<int:outfit_id>/',
         views.edit_outfit, name='edit_outfit'),
]

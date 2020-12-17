from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.productDetail, name='product_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart')
]

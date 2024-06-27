from .views import HomeView,ShopDetailView,ContactView,ShopView,cart,add_cart,sub_cart,remove_cart,chackout #new

from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('shop/<slug:slug>/', ShopDetailView.as_view(),name="detail-page"),
    path('shop/',ShopView.as_view(), name="shop-page"),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path('cart/', cart, name="cart"),
    path('chackout/',chackout, name='chackout'), #new
    path('cart/add_product/<int:product_id>/', add_cart, name="add-cart"),
    path('cart/sub_product/<int:product_id>/', sub_cart, name="sub-cart"),
    path('cart/remove_product/<int:product_id>/', remove_cart, name="remove-cart"),
]

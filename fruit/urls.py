from .views import HomeView,shop_view,ContactView

from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('shop/',shop_view,name="shop-page"),
    path("contact/",ContactView.as_view(),name="contact-page")
]
from .views import home_view,shop_view,contact_view

from django.urls import path

urlpatterns = [
    path('', home_view, name="home-page"),
    path('shop/',shop_view,name="shop-page"),
    path("contact/",contact_view,name="contact-page")
]
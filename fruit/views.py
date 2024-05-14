from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,"index.html")

def shop_view(request):
    return render(request,"shop.html")
def contact_view(request):
    return render(request,"contact.html")
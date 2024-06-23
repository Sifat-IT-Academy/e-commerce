from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse

from .forms import CommentForm
from .bot import send_message
from .models import Contact,Product,Category,Comment
from django.views.generic import View,TemplateView,DetailView,ListView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self,*args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['products'] = Product.objects.all()
        context['besteller_products'] = Product.objects.all().order_by('-rating')[:6] #new
        context['categories'] = Category.objects.all()
        context["reyting"] = [1,2,3,4,5]
        
        query = self.request.GET.get('q')
        if query:
            context['products'] = Product.objects.filter(title__icontains=query)

        return context

class ShopDetailView(DetailView):
    model = Product
    template_name = "shop-detail.html"
    context_object_name = "product"
    form_class = CommentForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = Comment.objects.filter(product=self.object).order_by("-created_date")
        context["form"] = self.form_class()
        context["reyting"] = [1,2,3,4,5]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)

        if form.is_valid():
            # Process form data
            full_name = form.cleaned_data['full_name']
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            email = form.cleaned_data['email']
            comment = Comment()
            comment.full_name = full_name
            comment.product = self.object
            comment.description = description
            comment.rating = rating
            comment.email = email
            comment.save()
            return redirect(self.object.get_absolute_url())
        else:
            print(form.errors)  # Xatolikni chop etish
        return self.render_to_response(self.get_context_data(form=form))


class ShopView(ListView):
    model = Product
    paginate_by = 2
    template_name = "shop.html"
    context_object_name ="Products"
    
    def get_queryset(self):
            queryset = super().get_queryset()
            min_price = self.request.GET.get('price')
            name = self.request.GET.get('q')
            if min_price:
                queryset = queryset.filter(price__lte=min_price)
            if name:
                queryset = queryset.filter(title__icontains=name)
            return queryset


class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(first_name=name,email=email,description=message)
        contact.save()
        
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        return HttpResponseRedirect(reverse('home-page'))   

def chackout(request):
    return render(request,"chackout.html")

def cart(request):
    return render(request,"cart.html")

from .forms import LoginForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})
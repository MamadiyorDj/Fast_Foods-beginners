from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import UserForm
from django.views import generic
from .models import *

# Create your views here.

#def register(request):
#   if request.method == 'POST':
#        form = UserForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect(reverse('register'))
#        context = {'form': form}
#        return render(request, 'register.html', context)
#    context = {'form': UserForm()}
#    return render(request, 'register.html', context)

class CategoryListView(generic.ListView):
    model = Categories
    template_name = 'base.html'
    context_object_name = 'categories'
    print(model)

def category(request,id):
    category = Products.objects.filter(category_id=id)
    print(category)
    return render(request, 'category_detail.html', context={'category':category})


class ProductListView(generic.ListView):
    model = Products
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'product_detail.html'
    context_object_name = 'product'


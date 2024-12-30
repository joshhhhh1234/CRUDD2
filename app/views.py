from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'app/customer_list.html'
    context_object_name = 'post_list'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'app/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    fields =  ['username', 'address']
    template_name = 'app/customer_create.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['username', 'address']
    template_name = 'app/customer_update.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_delete.html'
    success_url = reverse_lazy('customer')



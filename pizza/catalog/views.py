from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import CreateUser, LoginUser, PizzaForm
from catalog.models import Pizza
from cart.models import Cart


class CatalogView(TemplateView):
    template_name = 'catalog/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Pizza.objects.all()
        # фильтры
        filters = {i: self.request.GET[i] for i in self.request.GET if i.endswith('__exact')}
        queryset = queryset.filter(**filters)
        # сортировка
        if order := self.request.GET.get('order_by'):
            queryset = queryset.order_by(order)
        # поиск
        if name := self.request.GET.get('q'):
            queryset = queryset.filter(name__icontains=name)
        context['catalog_records'] = queryset
        # количество пиц в корзине
        if self.request.user.is_authenticated:
            context['cart_size'] = Cart.objects.filter(user=self.request.user).count()
        else: 
            context['cart_size'] = 0
        context['active'] = 'catalog'
        return context


class AuthorizationView(LoginView): 
    template_name = 'app/login.html'
    form_class = LoginUser 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'login'
        return context

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('catalog'))


class RegisterView(CreateView): 
    template_name = 'app/logup.html'
    form_class = CreateUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'login'
        return context

    def form_valid(self, form): 
        user = form.save()
        login(self.request, user)
        return redirect('catalog')


def logout_view(request): 
    logout(request)
    return redirect('catalog')


class AddPizzaView(CreateView): 
    model = Pizza
    form_class = PizzaForm
    template_name = 'catalog/pizza.html'
    success_url = reverse_lazy('add_pizza')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'add-pizza'
        return context


class PizzaView(UpdateView): 
    model = Pizza
    form_class = PizzaForm
    template_name = 'catalog/pizza.html'
    success_url = reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'add-pizza'
        return context


class DeletePizzaView(DeleteView): 
    model = Pizza
    success_url = reverse_lazy('catalog')

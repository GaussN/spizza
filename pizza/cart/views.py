from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, DeleteView

from catalog.models import Pizza
from cart.models import Cart


class CartView(LoginRequiredMixin, TemplateView): 
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_records'] = Cart.objects.filter(user=self.request.user)
        context['active'] = 'cart'
        return context


class DeleteCartRecord(LoginRequiredMixin, DeleteView): 
    model = Cart
    success_url = reverse_lazy('cart')


class CreateCartOrder(LoginRequiredMixin, View): 
    def post(self, request, pk, **kwargs):
        c_user = self.request.user 
        c_pizza = Pizza.objects.get(pk=pk)
        if not Cart.objects.filter(user=c_user).filter(pizza=c_pizza):
            new_order = Cart(user=c_user, pizza=c_pizza)
            new_order.save()
        return redirect('catalog') 


@require_POST
def crement(request, pk: int, ct=None): 
    cart_record = Cart.objects.get(pk=pk)
    match ct:
        case '+':
            cart_record.count += 1
        case '-':
            cart_record.count -= 1 if cart_record.count > 1 else 0
        case _:
            print(f'\nct is {ct}(must be a +/- )\n')
            return redirect('catalog')
    cart_record.save()
    return redirect('cart')


class ClearCart(LoginRequiredMixin, View): 
    def post(self, request):
        Cart.objects.filter(user=self.request.user).delete()   
        return redirect('cart')


class MakeOrderView(TemplateView): 
    template_name = 'cart/confirm-order.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['active'] = 'cart'
        orders = Cart.objects.filter(user=self.request.user)
        price = 0
        for o in orders:
            price += o.pizza.price * o.count
        context['price'] = price
        return context

    def post(self, request, **kwargs):
        # тут была бы логика оформления заказа
        return redirect('catalog')

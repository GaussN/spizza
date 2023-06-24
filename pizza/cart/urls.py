from django.urls import path

from cart import views


urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('delete/<int:pk>', views.DeleteCartRecord.as_view(), name='delete-cart-record'),
    path('new/<int:pk>', views.CreateCartOrder.as_view(), name='add-pizza-to-cart'),
    path('delete/all', views.ClearCart.as_view(), name='clear-cart'),
    path('increment/<int:pk>', views.crement, kwargs={'ct': '+'}, name='increment'),
    path('decrement/<int:pk>', views.crement, kwargs={'ct': '-'}, name='decrement'),
    path('make-order', views.MakeOrderView.as_view(), name='make-order'),
]

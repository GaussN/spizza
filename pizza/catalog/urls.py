"""
То же что и cart/urls.py
"""
from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('login', views.AuthorizationView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.logout_view, name='logout'),

    path('pizza/add', views.AddPizzaView.as_view(), name='add_pizza'),
    path('pizza/delete/<int:pk>', views.DeletePizzaView.as_view(), name='delete_pizza'),
    path('pizza/<int:pk>', views.PizzaView.as_view(), name='pizza'),
]

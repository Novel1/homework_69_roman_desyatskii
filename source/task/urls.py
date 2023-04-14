from django.urls import path
from task.view import add_view

from task.view import subtract_view, multiply_view, divide_view


urlpatterns = [
    path('add/', add_view, name='add_view'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide')
]
from django.urls import path
import re
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SYMBOL/<str:symbol>' ,views.base ,name='base' ),
]
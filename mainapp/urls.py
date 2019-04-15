from django.urls import path
import re
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SYMBOL/<str:symbol>' ,views.base ,name='base' ),
    path('SYMBOL/<str:symbol>/Analysis' ,views.analyse ,name='analyse' ),
    path('SYMBOL/<str:symbol>/Analysis/<str:analysis_type>/<int:period>/<str:unit>' ,views.analyse ,name='analyse' ),
    path('SYMBOL/<str:symbol>/Updatedata' ,views.update ,name='update' ),
    path('SYMBOL/<str:symbol>/Predict' ,views.predict ,name='predict' ),
]
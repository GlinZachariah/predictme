from django.urls import path
import re
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('?symbol=<str:symbol>',views.base ,name='base'),
    path('SYMBOL/<str:symbol>' ,views.base ,name='base' ),
    path('SYMBOL/<str:symbol>/Analysis' ,views.analyse ,name='analyse' ),
    path('SYMBOL/<str:symbol>/Analysis/<str:analysis_type>/<int:period>/<str:unit>' ,views.analyse ,name='analyse' ),
    path('SYMBOL/<str:symbol>/Updatedata' ,views.update ,name='update' ),
    path('SYMBOL/<str:symbol>/Predict' ,views.predict ,name='predict' ),
    path('SYMBOL/<str:symbol>/Predict/UpdateData' ,views.generateWeighted ,name='generateWeighted' ),
     path('SYMBOL/<str:symbol>/Predict/Download' ,views.generateCSV ,name='generateCSV' ),
    path('SYMBOL/<str:symbol>/Twitter' ,views.twitter ,name='twitter' ),
    path('SYMBOL/<str:symbol>/News' ,views.news ,name='news' ),
]


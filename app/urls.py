from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('adddata/',views.adddata, name='adddata'),
    path('delete/',views.datadelete, name='delete'),
]

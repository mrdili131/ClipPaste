from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='home'),
    path('data/<str:id>/',views.dataView, name='data')
]
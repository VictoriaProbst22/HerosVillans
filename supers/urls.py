from django.urls import path
from . import views

urlpatterns =[
    path('', views.Supers_list),
    path('<pk>/', views.supers_detail)
]
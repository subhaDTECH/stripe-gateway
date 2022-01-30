from . import views
from django.urls import path,include
urlpatterns = [
   
    path('', views.HomePageView.as_view(), name='home'),
    path('charge/', views.charge, name='charge'), # new
]
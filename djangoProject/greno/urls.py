from django.urls import path
from . import views

# localhost:8000/greno
# localhost:8000/greno/orders -->  path('orders/', views.orders, name='orders'),

urlpatterns = [
    path('', views.all_sectors, name='all_sectors'),

]
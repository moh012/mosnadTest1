from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userdata', views.userdata, name='userdata'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('pro', views.pro, name='pro'),
    path('pro_s/<int:id>', views.pro_s, name='pro_s'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
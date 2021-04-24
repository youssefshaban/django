from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login', obtain_auth_token),
    path('signup', views.apiSignup),
    path('create', views.Create),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('get/<int:id>', views.getByID),
    path('list', views.index),

]

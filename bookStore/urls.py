"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from rest_framework import routers
# from ..bookStore.api.views import BookViewSet
#
#
# router = routers.DefaultRouter()
# router.register('',)

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('createCat', views.createCat, name='createCat'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("api/books/", include("bookStore.api.urls")),
    # path('api/viewsets/books/', include(router.urls))

]

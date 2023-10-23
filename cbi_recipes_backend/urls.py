"""
URL configuration for cbi_recipes_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cbi_recipe_appplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_category_recipes/', views.get_category_recipes, name='get_category_recipes'),
    path('api/get_recipes_from_category/', views.get_recipes_from_category, name='get_recipes_from_category'),
    path('api/get_recipes_by_id/', views.get_recipes_by_id, name='get_recipes_by_id'),
]

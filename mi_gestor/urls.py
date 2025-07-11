"""
URL configuration for mi_gestor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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



from clients.views import list_clients, create_client, update_client, delete_client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients', list_clients, name='list_clients'),
    path('api/clients/create', create_client, name='create_client'),
    path('api/clients/<int:pk>/update', update_client, name='update_client'),
    path('api/clients/<int:pk>/delete', delete_client, name='delete_client'),
]


 
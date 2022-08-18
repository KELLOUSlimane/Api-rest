"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from actor.views import EmployeManage, EmployesManage, EntrepriseManage, EntreprisesManage, add_entreprise, affich_employes, affich_entreprise, add_employes, sup_entreprise, sup_employes, opd_employes, opd_Entreprise
from .views import index
urlpatterns = [
    path('', index, name='index'),

 
    path('entreprises', EntreprisesManage.as_view()),
    path('entreprises/<int:id>', EntrepriseManage.as_view()),
    path('emploi', EmployeManage.as_view()),
    path('employes/<int:id>', EmployesManage.as_view()),
    path('admin/', admin.site.urls),
]

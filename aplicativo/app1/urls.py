from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='app1'),
    path('storage/<str:nombre>/<str:apellido>/<int:edad>/<str:ocupacion>/<str:correo>/<str:documento>', views.storage, name='Principal'),
    path('storage2/<str:nombre>/<str:apellido>/<int:edad>/<int:principal_id>', views.storage2, name='Secundario')

]

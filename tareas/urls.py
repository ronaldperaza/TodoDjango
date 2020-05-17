from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('editar_tarea/<str:pk>', views.editar_tarea, name="editar_tarea"),
    path('eliminar_tarea/<str:pk>', views.eliminar_tarea, name="eliminar_tarea"),
]
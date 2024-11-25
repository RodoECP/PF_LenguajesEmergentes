from django.urls import path
from .views import LibroListView, IndexView, ObtenerAutoresView, ObtenerLibrosView, AgregarAutorView, AgregarLibroView, EliminarAutorView, EliminarLibroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('libros/', LibroListView.as_view(), name='libro_list'),
    path('obtener_autores/', ObtenerAutoresView.as_view(), name='obtener_autores'),
    path('obtener_libros/', ObtenerLibrosView.as_view(), name='obtener_libros'),
    path('agregar_autor/', AgregarAutorView.as_view(), name='agregar_autor'),
    path('agregar_libro/', AgregarLibroView.as_view(), name='agregar_libro'),
    path('eliminar_autor/<int:pk>/', EliminarAutorView.as_view(), name='eliminar_autor'),
    path('eliminar_libro/<int:pk>/', EliminarLibroView.as_view(), name='eliminar_libro'),
]

#Cambio hecho: importar y declarar vistas
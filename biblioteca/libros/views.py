from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View, ListView, CreateView, DeleteView
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# Vista para mostrar la lista de libros en el index
class LibroListView(ListView):
    model = Libro
    template_name = 'index.html'
    context_object_name = 'libros'

# Vista para la página de inicio
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

# Vista para obtener todos los autores en formato JSON
class ObtenerAutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        data = [{'id': autor.id, 'nombre': autor.nombre} for autor in autores]
        return JsonResponse({'data': data})

# Vista para obtener todos los libros en formato JSON
class ObtenerLibrosView(View):
    def get(self, request, *args, **kwargs):
        libros = Libro.objects.all()
        data = [{'id': libro.id, 'titulo': libro.titulo, 'autor': libro.autor.nombre} for libro in libros]
        return JsonResponse({'data': data})

# Vista para agregar un nuevo autor mediante un formulario
class AgregarAutorView(CreateView):
    model = Autor
    form_class = AutorForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 'ok'})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors})

# Vista para agregar un nuevo libro mediante un formulario
class AgregarLibroView(CreateView):
    model = Libro
    form_class = LibroForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 'ok'})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors})

# Vista para eliminar un autor específico
class EliminarAutorView(DeleteView):
    model = Autor
    def post(self, request, *args, **kwargs):       #Cambio hecho: delete cambiado por post ya que este tipo de acción solo acepta get y post
        try:
            self.get_object().delete()
            return JsonResponse({'status': 'ok'})
        except self.model.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Autor no encontrado'})

# Vista para eliminar un libro específico
class EliminarLibroView(DeleteView):
    model = Libro
    def post(self, request, *args, **kwargs):       #Cambio hecho: mismo que class EliminarAutorView
        try:
            self.get_object().delete()
            return JsonResponse({'status': 'ok'})
        except self.model.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Libro no encontrado'})
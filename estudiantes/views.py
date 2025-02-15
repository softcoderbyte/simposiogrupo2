from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render
from .models import Estudiante
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

def dashboard(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'dashboard.html', {'estudiantes': estudiantes})

# Crear estudiante
@csrf_exempt
def crear_estudiante(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        estudiante = Estudiante.objects.create(
            carnetcarrera=data['carnetcarrera'], carnetanio=data['carnetanio'], carnetcorrelativo=data['carnetcorrelativo'],
            nombre1=data['nombre1'], nombre2=data['nombre2'], apellido1=data['apellido1'], apellido2=data['apellido2'],
            telefono=data['telefono'], correo=data['correo'], pagado=data['pagado']
        )
        return JsonResponse({'mensaje': 'Estudiante creado'}, status=201)

# Obtener estudiantes
def obtener_estudiantes(request):
    estudiantes = Estudiante.objects.all().values()
    return JsonResponse(list(estudiantes), safe=False)

# Obtener estudiante por ID
def obtener_estudiante(request, id):
    try:
        estudiante = Estudiante.objects.get(id=id)
        return JsonResponse({'id': estudiante.id, 'carnetcarrera': estudiante.carnetcarrera, 'carnetanio': estudiante.carnetanio, 'carnetcorrelativo': estudiante.carnetcorrelativo, 'nombre1': estudiante.nombre1, 'nombre2': estudiante.nombre2, 'apellido1': estudiante.apellido1, 'apellido2': estudiante.apellido2, 'telefono': estudiante.telefono, 'correo': estudiante.correo, 'pagado': estudiante.pagado, 'fecharegistro': estudiante.fecharegistro})
    except Estudiante.DoesNotExist:
        return JsonResponse({'mensaje': 'Estudiante no encontrado'}, status=404)

from proyecto.models import Proyecto
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permisos_clases = [permissions.AllowAny]
    serializer_class = ProyectoSerializer
    
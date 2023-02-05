from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'nombre', 'permiso')
        # read_only_fields = ('id',)
        # F1000000F1E30000F1E3A500F1E3A51B
        # 42E3A51B4272A51B4272EE1B4272EE22
from rest_framework import viewsets
from usuarioApp.api.serializers import PersonasSerializer
from usuarioApp.models import Personas

class PersonasMVS(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer
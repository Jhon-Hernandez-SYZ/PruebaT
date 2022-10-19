

from rest_framework import serializers
from usuarioApp.models import Personas


class PersonasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = "__all__"

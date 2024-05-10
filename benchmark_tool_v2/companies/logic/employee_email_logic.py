from rest_framework import serializers
from ..models import EmployeeEmail
from rest_framework.validators import UniqueValidator

class EmployeeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEmail
        fields = "__all__"
        validators = [
            UniqueValidator(queryset=EmployeeEmail.objects.all())
        ]




# TODO send emails
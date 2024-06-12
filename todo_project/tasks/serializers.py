from rest_framework import serializers
from .models import Task
from tasks import models
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

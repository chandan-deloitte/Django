from rest_framework import serializers
from .models import Projects, Issues

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Projects
        fields = ('__all__')


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Issues
        fields = ('__all__')
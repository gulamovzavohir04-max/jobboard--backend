from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Job
        fields = ["id", "owner", "title", "company", "description", "salary", "location", "created_at"]

from rest_framework import serializers
from .models import AllFiles


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllFiles
        fields = "__all__"
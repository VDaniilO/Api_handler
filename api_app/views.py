from django.shortcuts import render
from rest_framework import generics
from .models import AllFiles
from .serializers import FilesSerializer


class FilesAPIList(generics.ListCreateAPIView):
    queryset = AllFiles.objects.all()
    serializer_class = FilesSerializer

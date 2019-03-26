from django.shortcuts import render
from rest_framework import viewsets
from oxxo.serializers import ChelaSerializer
from .models import Chela


class ChelaViewSet(viewsets.ModelViewSet):

    serializer_class = ChelaSerializer
    queryset = Chela.objects.all()
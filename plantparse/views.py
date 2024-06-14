from rest_framework import viewsets
from .models import PlantsAll
from .serializers import PlantsAllSerializer
from rest_framework.response import Response

class PlantsAllViewSet(viewsets.ModelViewSet):
    queryset = PlantsAll.objects.all()
    serializer_class = PlantsAllSerializer

class AloeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlantsAll.objects.filter(plant_name_latin='Aloe vera')
    serializer_class = PlantsAllSerializer
    lookup_field = 'plant_name_latin'

class AeoniumViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlantsAll.objects.filter(plant_name_latin='Aeonium arboreum')
    serializer_class = PlantsAllSerializer
    lookup_field = 'plant_name_latin'


from rest_framework import serializers
from .models import PlantsAll, PlantsEn, PlantsHy

class PlantsEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantsEn
        fields = '__all__'

class PlantsHySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantsHy
        fields = '__all__'

class PlantsAllSerializer(serializers.ModelSerializer):
    plant_name_en = PlantsEnSerializer()
    plant_name_hy = PlantsHySerializer()

    class Meta:
        model = PlantsAll
        fields = '__all__'
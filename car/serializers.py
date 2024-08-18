from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=1, max_value=2000)  # Example range for horsepower
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(allow_null=True, required=False)

    def create(self, validated_data):
        return Car(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.model = validated_data.get('model', instance.model)
        instance.horse_powers = validated_data.get('horse_powers', instance.horse_powers)
        instance.is_broken = validated_data.get('is_broken', instance.is_broken)
        instance.problem_description = validated_data.get('problem_description', instance.problem_description)
        instance.save()
        return instance

from rest_framework import serializers


class ApplicationTourSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=60, required=True)
    phone_number = serializers.CharField(max_length=30, required=True)
    tour = serializers.IntegerField(min_value=1, required=True)
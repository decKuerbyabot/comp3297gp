from rest_framework import serializers
from .models import *

class RecordSerialzer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.leave_datetime=validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance
    class Meta:
        model=Record
        fields='__all__'

class VenueSerializer(serializers.ModelSerializer):
    venue_code = serializers.Field(source='venue_code')
    class Meta:
        model=Venue
        fields = '__all__'


class HKUmemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=HKUMember
        fields = '__all__'

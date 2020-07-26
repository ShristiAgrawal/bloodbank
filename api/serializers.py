from rest_framework import serializers

from .models import A

class ASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = A
        fields = ('name', 'phone')
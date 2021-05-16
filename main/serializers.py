from rest_framework import serializers
from .models import Lawyer, Civilian

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ['firstname','lastname','image','phone','location']

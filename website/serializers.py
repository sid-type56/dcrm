from rest_framework import serializers
from .models import WebUser



class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model:WebUser
        fields = '__all__'
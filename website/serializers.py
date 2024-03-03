from rest_framework import serializers
from .models import User



class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model:User
        fields = '__all__'
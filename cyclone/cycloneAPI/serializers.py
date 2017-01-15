from rest_framework import serializers
from .models import user

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'full_name', 'email', 'Password')


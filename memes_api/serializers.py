from rest_framework import serializers
from .models import Meme, MemeNoImg

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ('id', 'name', 'description', 'image')


class MemeNoImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemeNoImg
        fields = ('id', 'name', 'description')
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


# v2
class BaseUserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')


# v1
class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')

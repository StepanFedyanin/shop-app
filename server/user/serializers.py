from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, ListField, IntegerField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import MyUser


class MyUserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = MyUser
        fields = ('id', 'email', 'password', 'last_login')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

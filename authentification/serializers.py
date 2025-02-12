from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from authentification.models import User


class UserSerializer(ModelSerializer):
    
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ["id", "username", "password", "age", "can_be_contacted", "can_data_be_shared"]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

from rest_framework.serializers import ModelSerializer

from authentification.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "age", "can_be_contacted", "can_data_be_shared"]

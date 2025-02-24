from rest_framework.viewsets import ModelViewSet

from authentification.models import User
from authentification.serializers import UserSerializer
from authentification.serializers import UserUpdateSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return UserUpdateSerializer
        else:
            return super().get_serializer_class()

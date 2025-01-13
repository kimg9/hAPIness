from rest_framework.viewsets import ModelViewSet

from authentification.models import User
from authentification.serializers import UserSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

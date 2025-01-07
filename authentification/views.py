from rest_framework.viewsets import ModelViewSet

from authentification.models import User
from authentification.serializers import UserSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.GET.get('id')
        if user_id is not None:
            queryset = queryset.filter(id=user_id)
        return queryset

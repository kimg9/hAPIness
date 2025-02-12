from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from . import permissions
from .serializers import ProjectSerializer
from .serializers import IssueSerializer
from .serializers import CommentSerializer
from .models import Project
from .models import Issue
from .models import Comment
from .models import Contributor
from rest_framework.exceptions import ValidationError


# READ & MODIFY: User qui est Contributeur et qui a le Project dans ses projets
# CREATE : Anyone ?
# MODIFY & DELETE : auteur
class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        request_user = self.request.user
        contributor, _ = Contributor.objects.get_or_create(user=request_user)
        project = serializer.save(author=request_user)
        contributor.projects.add(project)
        contributor.save()


# READ : User qui est Contributeur et qui a le Project dans ses projets
# CREATE : User qui est Contributeur et qui a le Project dans ses projets
# MODIFY & DELETE : auteur
class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

    def perform_create(self, serializer):
        # TODO : Check if user has perm to create
        contributors = Contributor.objects.filter(projects=serializer.validated_data["project"])
        if serializer.validated_data["user_attribution"] not in (
            contributor.user for contributor in contributors
        ):
            raise ValidationError(
                "L'utilisateur attribué n'est pas un contributeur du projet."
            )

        serializer.save(author=self.request.user)


# READ : User qui est Contributeur et qui a le Project dans ses projets
# CREATE : User qui est Contributeur et qui a le Project dans ses projets
# MODIFY & DELETE : auteur
class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        # TODO : Check if user has perm to create
        serializer.save(author=self.request.user)

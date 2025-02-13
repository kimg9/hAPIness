from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Contributor, Issue, Project
from .permissions import IsOwnerOfItem
from .permissions import IsProjectContributor
from .permissions import IsProjectContributorOfIssue
from .permissions import IsProjectContributorOfComment
from .permissions import AnyoneCanRegister
from .serializers import CommentSerializer, IssueSerializer, ProjectSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [AnyoneCanRegister, IsProjectContributor, IsOwnerOfItem]

    def perform_create(self, serializer):
        request_user = self.request.user
        project = serializer.save(author=request_user)
        contributor, _ = Contributor.objects.get_or_create(user=request_user)
        contributor.projects.add(project)
        contributor.save()


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [IsOwnerOfItem, IsProjectContributorOfIssue]

    def perform_create(self, serializer):
        contributors = Contributor.objects.filter(
            projects=serializer.validated_data["project"]
        )
        if serializer.validated_data["user_attribution"] not in (
            contributor.user for contributor in contributors
        ):
            raise ValidationError(
                "L'utilisateur attribué n'est pas un contributeur du projet."
            )

        serializer.save(author=self.request.user)


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOfItem, IsProjectContributorOfComment]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

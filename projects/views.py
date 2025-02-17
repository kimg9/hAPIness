from rest_framework.viewsets import ModelViewSet

from .models import Comment, Contributor, Issue, Project
from .permissions import (IsOwnerOfItem, IsProjectContributor,
                          IsProjectContributorOfComment,
                          IsProjectContributorOfIssue)
from .serializers import CommentSerializer, IssueSerializer, ProjectSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectContributor | IsOwnerOfItem]
    
    def get_queryset(self):
        return Project.objects.filter(contributor__user=self.request.user)

    def perform_create(self, serializer):
        request_user = self.request.user
        project = serializer.save(author=request_user)
        contributor, _ = Contributor.objects.get_or_create(user=request_user)
        contributor.projects.add(project)
        contributor.save()


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsOwnerOfItem | IsProjectContributorOfIssue]
    
    def get_queryset(self):
        return Issue.objects.filter(project__contributor__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOfItem | IsProjectContributorOfComment]
    
    def get_queryset(self):
        return Comment.objects.filter(issue__project__contributor__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

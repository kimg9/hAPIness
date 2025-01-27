from rest_framework.viewsets import ModelViewSet

from projects.serializers import ProjectSerializer
from projects.serializers import IssueSerializer
from projects.serializers import CommentSerializer
from projects.serializers import ContributorSerializer
from projects.models import Project
from projects.models import Issue
from projects.models import Comment
from projects.models import Contributor


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()

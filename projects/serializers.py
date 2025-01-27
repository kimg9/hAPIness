from rest_framework.serializers import ModelSerializer

from projects.models import Project
from projects.models import Issue
from projects.models import Comment
from projects.models import Contributor


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor

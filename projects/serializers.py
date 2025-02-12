from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from projects.models import Project
from projects.models import Issue
from projects.models import Comment
from projects.models import Contributor


class ProjectSerializer(ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('author', 'created_time')


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ('author', 'created_time')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'created_time')

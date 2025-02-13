from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Contributor


class IsOwnerOfItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "PUT" or request.method == "DELETE":
            return obj.author == request.user
        return False


class AnyoneCanRegister(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True


class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            contributor = get_object_or_404(Contributor, user=request.user)
            return obj in contributor.project
        return False


class IsProjectContributorOfIssue(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            contributor = get_object_or_404(Contributor, user=request.user)
            return obj.project in contributor.project
        return False


class IsProjectContributorOfComment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "POST":
            contributor = get_object_or_404(Contributor, user=request.user)
            return obj.issue.project in contributor.project
        return False

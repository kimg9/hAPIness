from rest_framework import permissions

from .models import Contributor

CONSULT_OR_CREATE_METHODS = (
    "GET",
    "POST",
    "PATCH"
)

class IsOwnerOfItem(permissions.BasePermission):
    ACCEPTED_METHODS = (
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "PATCH"
    )
    def has_object_permission(self, request, view, obj):
        if request.method in self.ACCEPTED_METHODS:
            return obj.author == request.user
        return False

class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in CONSULT_OR_CREATE_METHODS:
            return obj.contributor_set.filter(user=request.user).exists()
        return False


class IsProjectContributorOfIssue(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in CONSULT_OR_CREATE_METHODS:
            return obj.project.contributor_set.filter(user=request.user).exists()
        return False


class IsProjectContributorOfComment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in CONSULT_OR_CREATE_METHODS:
            return obj.issue.project.contributor_set.filter(user=request.user).exists()
        return False

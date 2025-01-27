from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from authentification.views import UserViewset
from projects.views import ProjectViewset
from projects.views import IssueViewset
from projects.views import CommentViewset
from projects.views import ContributorViewset

router = routers.SimpleRouter()
router.register("user", UserViewset, basename="user")
router.register("project", ProjectViewset, basename="project")
router.register("issue", IssueViewset, basename="issue")
router.register("comment", CommentViewset, basename="comment")
router.register("contributor", ContributorViewset, basename="contributor")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]

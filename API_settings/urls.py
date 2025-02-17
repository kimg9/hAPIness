from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from authentification.views import UserViewset
from projects.views import CommentViewset, IssueViewset, ProjectViewset

router = routers.SimpleRouter()
router.register("user", UserViewset, basename="user")
router.register("project", ProjectViewset, basename="project")
router.register("issue", IssueViewset, basename="issue")
router.register("comment", CommentViewset, basename="comment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

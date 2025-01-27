from django.db import models
from authentification.models import User
import uuid


class Project:
    class ProjectTypes(models.TextChoices):
        BACKEND = "back-end"
        FRONTEND = "front-end"
        IOS = "iOS"
        ANDROID = "Android"

    author = models.ForeignKey(null=True, to=User)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    project_type = models.CharField(null=True, choices=ProjectTypes.choices)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor:
    user = models.ForeignKey(null=True, to=User)
    projects = models.ManyToManyField(null=True, to=Project)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue:
    class PriorityChoices(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    class StatusChoices(models.TextChoices):
        TODO = "To Do"
        IN_PROGRESS = "In Progress"
        FINISHED = "Finished"

    class BaliseChoices(models.TextChoices):
        BUG = "BUG"
        TASK = "TASK"
        FEATURE = "FEATURE"

    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    project = models.ForeignKey(null=True, to=Project)
    status = models.CharField(
        max_length=250, null=False, choices=StatusChoices.choices, default=1
    )
    priority = models.CharField(null=True, choices=PriorityChoices.choices)
    balise = models.CharField(null=True, choices=BaliseChoices.choices)
    created_time = models.DateTimeField(auto_now_add=True)
    user_attribution = models.ForeignKey(null=True, to=User)
    author = models.ForeignKey(null=True, to=User)


class Comment:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(null=True, to=Issue)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(null=True, to=User)

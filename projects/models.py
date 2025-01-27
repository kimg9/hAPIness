from django.db import models
from authentification.models import User
import uuid


class Project(models.Model):
    class ProjectTypes(models.TextChoices):
        BACKEND = "back-end"
        FRONTEND = "front-end"
        IOS = "iOS"
        ANDROID = "Android"

    author = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    project_type = models.CharField(max_length=10, null=True, choices=ProjectTypes.choices)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    user = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
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
    project = models.ForeignKey(null=False, to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, null=False, choices=StatusChoices.choices, default=StatusChoices.TODO)
    priority = models.CharField(max_length=10, null=True, choices=PriorityChoices.choices)
    balise = models.CharField(max_length=10, null=True, choices=BaliseChoices.choices)
    created_time = models.DateTimeField(auto_now_add=True)
    user_attribution = models.ForeignKey(null=True, to=User, on_delete=models.SET_NULL, related_name="attributed_issues")
    author = models.ForeignKey(null=False, to=User, on_delete=models.CASCADE, related_name="created_issues")


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(null=True, to=Issue, on_delete=models.CASCADE)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)

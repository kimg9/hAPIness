from django.db import models
from authentification.models import User
import uuid


class Project:
    PROJECTS_TYPES = ((1, "back-end"), (2, "front-end"), (3, "iOS"), (4, "Android"))
    author = models.ForeignKey(null=True, to=User)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    project_type = models.IntegerField(null=True, choices=PROJECTS_TYPES)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor:
    user = models.ForeignKey(null=True, to=User)
    projects = models.ManyToManyField(null=True, to=Project)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue:
    PRIORITY_CHOICES = ((1, "LOW"), (2, "MEDIUM"), (3, "HIGH"))
    STATUS_CHOICES = ((1, "To Do"), (2, "In Progress"), (3, "Finished"))
    BALISE_CHOICES = (
        (1, "BUG"),
        (2, "TASK"),
        (3, "FEATURE"),
    )
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    project = models.ForeignKey(null=True, to=Project)
    status = models.IntegerField(
        max_length=250, null=False, choices=STATUS_CHOICES, default=1
    )
    priority = models.CharField(null=True, choices=PRIORITY_CHOICES)
    balise = models.IntegerField(null=True, choices=BALISE_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)
    user_attribution = models.ForeignKey(null=True, to=User)
    author = models.ForeignKey(null=True, to=User)


class Comment:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(null=True, to=Issue)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(null=True, to=User)

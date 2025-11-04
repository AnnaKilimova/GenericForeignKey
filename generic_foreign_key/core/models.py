from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class ActionLog(models.Model):
    '''Action Log model.

    Represents a record of an action performed by a user on any model instance.
    This model uses Django’s generic relationships to associate logs dynamically
    with different content types (e.g., Post, Comment, Profile).

    Each log entry captures:
      - The type of action (create, update, or delete)
      - The user who performed the action
      - The timestamp when the action occurred
      - A reference to the affected object (via GenericForeignKey)

    Attributes:
        action_type: CharField
            Indicates the kind of action performed. Supported values:
            - "create" — when an object is created
            - "update" — when an object is modified
            - "delete" — when an object is deleted

        timestamp: DateTimeField
            Automatically stores the timestamp when the log entry was created.

        user: ForeignKey
            The user who performed the action. If the user is deleted,
            their associated log entries are also deleted (CASCADE).
            Reverse access via `user.user_actionlog.all()`.

        content_type: ForeignKey
            References the Django ContentType for the related model.
            Defines the type of the object that this log refers to (e.g., Post, Comment).

        object_id: PositiveIntegerField
            Stores the primary key of the related object instance.

        content_object: GenericForeignKey
            A dynamic link to the actual object being referenced, defined by
            `content_type` and `object_id`.

    Notes:
        - This model enables tracking of user activity across multiple models.
        - Use `GenericRelation` on related models (e.g., Post, Profile) for
        reverse access to their logs.
    '''
    action_type = models.CharField(
        max_length=10,
        choices=[
            ('create', 'Create'),
            ('update', 'Update'),
            ('delete', 'Delete')
        ])
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_actionlog')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self) -> str:
        """Return a human-readable representation of the action log entry."""
        return f"{self.user.username} - {self.action_type} ({self.content_type} #{self.object_id})"

    class Meta:
        verbose_name = "Action Log"
        verbose_name_plural = "Action Logs"
        ordering = ("-timestamp",)
        indexes = [
            models.Index(fields=["timestamp"]),
            models.Index(fields=["action_type"]),
        ]

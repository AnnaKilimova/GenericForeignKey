from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.contenttypes.fields import GenericRelation


class Profile(models.Model):
    '''User Profile model.

    Represents a user profile that extends the built-in User model with
    additional personal details such as biography, city, and date of birth.
    Also includes a generic relation to the ActionLog model to track
    user-related actions.

    Attributes:
        user: OneToOneField
            One-to-one relationship with the User model. Ensures that each user
            has exactly one profile. When the user is deleted, the related profile
            is automatically removed (via CASCADE).

        biography: TextField
            Optional text field for storing a short biography or personal note.
            Can be left empty in forms (blank=True).

        city: CharField
            Short text field (up to 30 characters) to store the user's city.

        birth_date: DateField
            Optional field storing the user's date of birth.
            Allows NULL in the database and can be empty in forms.

        logs: GenericRelation
            Generic relation to the ActionLog model (defined in `core.ActionLog`).
            This enables reverse lookups like `profile.logs.all()` to access
            log entries linked to this profile.

    Notes:
        - The GenericRelation does not create a new field in the database;
        it is used for reverse access to a GenericForeignKey in ActionLog.
        - Use `select_related("user")` to optimize queries when accessing
        user information frequently.
        - To manage logs for this profile, you can query:
            `ActionLog.objects.filter(content_type=..., object_id=profile.id)`
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    city = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Date of birth')
    logs = GenericRelation('core.ActionLog')

    def __str__(self) -> str:
        '''Returns a human-readable string representation of the profile.'''
        return f"{self.user.username}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("user__username",)

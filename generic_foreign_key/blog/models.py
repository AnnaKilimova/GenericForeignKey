from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model):
    '''Blog Post model.

    Represents a blog post created by a user. Each post includes a title,
    content body, timestamps for creation and modification, and a reference
    to its author. The model also maintains a generic relation to the
    ActionLog model, which allows logging and tracking of user actions
    related to posts (e.g., creation, update, deletion).

    Attributes:
        title: CharField
            The title of the post. Limited to 200 characters.

        content: TextField
            The main body text of the post. This field is required (blank=False).

        created_at: DateTimeField
            Automatically stores the timestamp when the post is first created.

        updated_at: DateTimeField
            Automatically stores the timestamp when the post is last modified.

        author: ForeignKey
            A foreign key linking to the User model. Each post belongs to one user.
            If the user is deleted, all their posts are deleted (CASCADE).
            The related name `user_post` allows reverse access via `user.user_post.all()`.

        logs: GenericRelation
            Generic relation to the ActionLog model (core.ActionLog). Enables access
            to log entries associated with this post via `post.logs.all()`.

    Notes:
        - Use `select_related("author")` in queries to optimize performance.
        - When displaying posts in templates, consider truncating `content`
        for summaries or previews.
    '''
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    logs = GenericRelation('core.ActionLog')

    def __str__(self) -> str:
        '''Return a human-readable string representation of the post.'''
        return f"{self.author.username} - {self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["created_at"]),
        ]
        constraints = [
            models.CheckConstraint(check=~models.Q(title=""), name="post_title_not_empty")
        ]


class Comment(models.Model):
    '''Comment model.

    Represents a comment made by a user on a specific post. Each comment is linked
    to a post and an author, includes text content, and stores its creation time.
    The model also includes a generic relation to ActionLog to track actions
    (e.g., creation, deletion, edits) performed on comments.

    Attributes:
        post: ForeignKey
            The post that this comment belongs to. Deleting the post removes
            all related comments (CASCADE). Reverse access via `post.post_comment.all()`.

        author: ForeignKey
            The user who wrote the comment. If the user is deleted, the comment
            is also deleted. Reverse access via `user.user_comment.all()`.

        content: TextField
            The main text of the comment. Required (blank=False).

        created_at: DateTimeField
            Automatically stores the timestamp when the comment was created.

        logs: GenericRelation
            Generic relation to the ActionLog model (core.ActionLog).
            Allows querying all logs associated with this comment using `comment.logs.all()`.

    Notes:
        - Comments are ordered by creation time (oldest first by default).
        - Use `select_related("post", "author")` for efficient querying.
        - Can be extended to support nested replies if needed.
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    logs = GenericRelation('core.ActionLog')

    def __str__(self) -> str:
        '''Return a human-readable string representation of the comment.'''
        return f"{self.author.username}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("created_at",)
        indexes = [
            models.Index(fields=["created_at"]),
        ]

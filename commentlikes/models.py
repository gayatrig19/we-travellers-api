from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class CommentLike(models.Model):
    """
    CommentLike model, related to User and Comment.
    Enables user to like the comments on the posts.
    'unique_together' makes sure a user can't 
    like the same comment twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment,
        related_name='commentlikes',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f'{self.owner} {self.comment}'
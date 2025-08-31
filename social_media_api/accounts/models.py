# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


class User(AbstractUser):
    """
    Custom user. We'll expose a 'following' M2M via a through model (Follow)
    so we can store timestamps and enforce constraints.
    """
    # Many-to-many to self through Follow (symmetrical=False)
    following = models.ManyToManyField(
        "self",
        through="accounts.Follow",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    @property
    def followers_count(self) -> int:
        return self.followers_relations.count()

    @property
    def following_count(self) -> int:
        return self.following_relations.count()


class Follow(models.Model):
    """
    Join table for follow relationships.
    follower -> followed
    """
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following_relations"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers_relations"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "followed")
        constraints = [
            models.CheckConstraint(
                check=~Q(follower=models.F("followed")),
                name="prevent_self_follow",
            )
        ]

    def __str__(self):
        return f"{self.follower.username} → {self.followed.username}"

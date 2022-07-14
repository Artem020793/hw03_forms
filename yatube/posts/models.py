from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    RELATED_NAME = 'posts'
    text = models.TextField(
        blank=False,
        null=False,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name=RELATED_NAME,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name=RELATED_NAME,
    )

    class Meta:
        ordering = ('-pub_date',)

from django.db import models
from django.contrib.auth.models import User


class BoardsModel(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def displayUser(self):
        return self.author.username

    displayUser.short_description = "author"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "DOC_BOARDS"

from email.policy import default
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thmb
    thumb = models.ImageField(default='default.png', blank=True)
    # add author

    def __str__(self):
        return self.title

    def sinppet(self):
        return self.body[:50] + "..."

from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    detail = models.TextField()
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    highlighted = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

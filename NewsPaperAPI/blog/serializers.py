from rest_framework import serializers
from .models import Paper, Post
from django.contrib.auth.models import User


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        # fields = '__all__'
        fields = ['id', 'title', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'detail','owner', 'paper', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

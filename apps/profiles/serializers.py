from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Profile, Post, Comment

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ['avatar', 'bio', 'city', 'birth_date', 'gender', 'relationship']
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']


class PostSerializer(serializers.ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Post
        # exclude = []
        fields = ['author', 'text', 'image']


class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Comment
        fields = "__all__"
        # exclude = ['post']

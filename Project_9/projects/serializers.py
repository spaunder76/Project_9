from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = '__all__'

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Issue
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = '__all__'

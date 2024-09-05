from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)

from .permissions import IsOwnerOrReadOnly

from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        # Only show projects where the user is a contributor
        return self.queryset.filter(contributors__user=self.request.user)

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Contributor.objects.filter(project__contributors__user=self.request.user)

    def perform_create(self, serializer):
        project_id = self.request.data.get("project")
        project = Project.objects.get(id=project_id)
        if not project.contributors.filter(user=self.request.user).exists():
            return Response(
                {"error": "You are not a contributor to this project"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer.save()


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        else:
            author_issues = self.queryset.filter(author=user)
            contributor_issues = self.queryset.filter(project__contributors__user=user)

            if author_issues.exists():
                return author_issues
            else:
                return contributor_issues


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        else:
            author_comments = self.queryset.filter(author=user)
            contributor_comments = self.queryset.filter(
                issue__project__contributors__user=user
            )

            if author_comments.exists():
                return author_comments
            else:
                return contributor_comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

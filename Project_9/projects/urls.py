from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"contributors", ContributorViewSet)
router.register(r"issues", IssueViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

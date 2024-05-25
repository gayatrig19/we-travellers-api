from rest_framework import generics, permissions
from we_travellers_api.permissions import IsOwnerOrReadOnly
from .models import CommentLike
from .serializers import CommentLikeSerializer


class CommentLikeList(generics.ListCreateAPIView):
    """
    List all likes on comments or create a like
    if user is logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment like.
    Delete it by id if a user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

from django.db.models import Count
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from we_travellers_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        commentlikes_count=Count('commentlikes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        """
        Method to make sure that comments are associated
        with a user upon creation.
        """
        serializer.save(owner=self.request.user)
        

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment. 
    Update or delete a comment by id if you are the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        commentlikes_count=Count('commentlikes', distinct=True)
    ).order_by('-created_at')
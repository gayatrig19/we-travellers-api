from rest_framework import generics, permissions
from we_travellers_api.permissions import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    """
    List all Bookmarks.
    Enable user to create a bookmark
    (bookmark posts) if user is logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a Bookmark or delete(remove)
    it by id if a user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
from django.db import IntegrityError
from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model
    The create method handles the unique constraint on
    'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        Allows user to create a bookmark.
        Returns a complete object instance if data is valid.
        A method to prevent users from creating duplicate bookmarks.
        Interity error is raised if user bookmarks the
        same post twice.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
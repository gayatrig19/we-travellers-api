from django.db import IntegrityError
from rest_framework import serializers
from .models import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the CommentLike model
    The create method handles the unique 
    constraint on 'owner' and 'comment'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLike
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        """
        Allows user to create a likes on comments.
        Returns a complete object instance
        if data is valid.
        A method to prevent users from creating
        duplicate likes on comments.
        Interity error is raised if user likes the
        same comment twice.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
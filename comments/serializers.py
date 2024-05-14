from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from commentlikes.models import CommentLike

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url')
    commentlike_id = serializers.SerializerMethodField()
    commentlikes_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        A method that returns how long ago
        a comment was created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        A method that returns how long ago
        a comment was updated.
        """
        return naturaltime(obj.updated_at)

    def get_commentlike_id(self, obj):
        """
        Method to let us know if the current user
        has already liked a comment.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            commentlike = CommentLike.objects.filter(
                owner=user, comment=obj
            ).first()
            return commentlike.id if commentlike else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'post', 'created_at',
            'updated_at', 'content', 'commentlike_id',
            'commentlikes_count'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view.
    Post is a read only field so that we dont have 
    to set it on each update.
    """
    post = serializers.ReadOnlyField(source='post.id')
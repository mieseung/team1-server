from rest_framework import serializers

from django.contrib.auth.models import User
from post.models import Post, PostReaction, Comment
# from user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='user.id', read_only=True)
    userFirstName = serializers.CharField(source='user.first_name', read_only=True)
    userLastName = serializers.CharField(source='user.last_name', read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'createdAt',
            'updatedAt',
            'userId',
            'userFirstName',
            'userLastName',
            'user_id',
        )

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=validated_data.pop('user_id'))
        return super(PostSerializer, self).create(validated_data)

class PostDetailSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='user.id')
    userFirstName = serializers.CharField(source='user.first_name')
    userLastName = serializers.CharField(source='user.last_name')
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'createdAt',
            'updatedAt',
            'userId',
            'userFirstName',
            'userLastName',
            'comments',
        )

    # def get_post_reactions(self, post):
    
    def get_comments(self, post):
        return CommentSerializer(post.comments, many=True).data

# class PostReactionSerializer(serializers.ModelSerializer):

class CommentSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='user.id', read_only=True)
    userFirstName = serializers.CharField(source='user.first_name', read_only=True)
    userLastName = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'userId',
            'userFirstName',
            'userLastName',
            'createdAt',
            'updatedAt',
        )

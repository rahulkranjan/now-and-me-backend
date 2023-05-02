from rest_framework import serializers

from posts.models import Reply, Thought
from users.models import User


class ThoughtSerializer(serializers.ModelSerializer):

    replys = serializers.SerializerMethodField()

    class Meta:
        model = Thought
        fields = '__all__'
        extra_fields = ['replys']

    # if is_anonymous is true, then author is anonymous
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['is_anonymous'] == True:
            representation['author'] = {
                'name': 'Anonymous',
                'avatar': None
            }
        else:
            representation['author'] = User.objects.filter(id=representation['author']).values('name', 'avatar')[0]
        return representation

    def get_replys(self, instance):
        replys = Reply.objects.filter(thought=instance.id)
        return ReplySerializer(replys, many=True).data


class ThoughtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

    # if is_anonymous is true, then author is anonymous
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['is_anonymous'] == True:
            representation['author'] = {
                'name': 'Anonymous',
                'avatar': None
            }
        else:
            representation['author'] = User.objects.filter(id=representation['author']).values('name', 'avatar')
        return representation
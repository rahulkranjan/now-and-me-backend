from rest_framework import serializers

from posts.models import Reply, Thought
from users.models import User


class ThoughtSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Thought
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['is_anonymous'] == True:
            representation['user'] = {
                'name': 'Anonymous',
                'avatar': None
            }
        else:
            representation['user'] = User.objects.filter(id=representation['user']).values('name', 'avatar')[0]
        return representation


class ThoughtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
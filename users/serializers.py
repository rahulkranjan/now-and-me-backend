from rest_framework import serializers
from .models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class TokenUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(read_only=True)
    organisation = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'roles', 'contact',
                  'avatar', 'date_joined', 'organisation')
        extra_kwargs = {'password': {'write_only': True}}

    

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer()
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'contact', 'password',
                  'roles')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):

        instance.name = validated_data.get(
            'name', instance.name)
        instance.contact = validated_data.get(
            'contact', instance.contact)
        instance.email = validated_data.get(
            'email', instance.email)

        instance.save()
        return instance


class UserSerializerDetailed(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)

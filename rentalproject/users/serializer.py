from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    full_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Users
        fields = ["id", "name", "email", "age", "bio", "password", "full_info"]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def get_full_info(self, obj):
        return f"{obj.name} ({obj.email})"

    def validate(self, data):
        if data['name'].lower() == data['email'].split('@')[0].lower():
            raise serializers.ValidationError(
                "Name and email should not be same")
        return data

    def validate_age(self, value):
        if value < 10:
            raise serializers.ValidationError("Age must be greater than 10")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

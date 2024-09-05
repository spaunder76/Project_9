# from rest_framework import serializers
# from users.models import NewUser


# class RegisterUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = NewUser
#         fields = ('email', 'user_name', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance


from rest_framework import serializers
from users.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(write_only=True, required=True)
    consent = serializers.ChoiceField(
        choices=["compactable", "shareable"], write_only=True, required=True
    )

    class Meta:
        model = NewUser
        fields = ("email", "user_name", "password", "age", "consent")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_age(self, value):
        """Ensure the user is at least 18 years old."""
        if value < 18:
            raise serializers.ValidationError(
                "You must be at least 18 years old to register."
            )
        return value

    def create(self, validated_data):
        """Create a new user instance."""
        # Remove 'age' and 'consent' after validation as they're not part of the user model
        validated_data.pop("age", None)
        validated_data.pop("consent", None)
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

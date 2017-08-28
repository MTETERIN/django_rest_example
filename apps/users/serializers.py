from rest_framework import serializers

from apps.core.utils import generate_unique_key, send_email_job
from apps.users.models import User
from apps.users.validators import check_valid_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    @staticmethod
    def send_mail(validated_data):
        """
        Generates a reset_key for changing password,
        Send and email to user with reset_key link.
        """
        user = User.objects.get(email=validated_data['email'])
        user.reset_key = generate_unique_key(user.email)
        user.save()
        send_email_job(
            user.email,
            'reset_password',
            {
                'reset_key': user.reset_key
            },
            'Reset Password',
        )

    def validate(self, data):
        self.check_email(data['email'])

        return data

    @staticmethod
    def check_email(value):
        """
        Check for not existing or inactive users.
        """
        user = User.objects.filter(email=value)

        if not user.exists():
            raise serializers.ValidationError('This email address does not exist.')

        if not user.filter(is_active=True).exists():
            raise serializers.ValidationError('Your account is inactive.')

        return value


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
    company = serializers.CharField()
    phone = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    @staticmethod
    def save_user(validated_data):
        """
        Saving signed up user to db,
        Send email address confirmation email to user.
        """
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.is_active = False
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.is_active = False
        user.email_confirmation_token = generate_unique_key(user.email)
        user.save()
        send_email_job(
            user.email,
            'account_confirmation',
            {
                'token': user.email_confirmation_token
            },
            'Email Confirmation',
        )

    def validate(self, data):
        """
        Validating user's data.
        :param data:
        :return: Validated data.
        """
        check_valid_password(data)
        self.check_valid_email(data['email'])

        return data

    @staticmethod
    def check_valid_email(value):
        """
        Validating user's email
        :param value:
        :return: Validated data.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address has already exist.')

        return value


class ConfirmAccountSerializer(serializers.Serializer):
    token = serializers.CharField()

    @staticmethod
    def confirm(validated_data):
        user = User.objects.get(email_confirmation_token=validated_data['token'])
        user.is_active = True
        user.email_confirmation_token = None
        user.save()

    def validate(self, data):
        if not User.objects.filter(email_confirmation_token=data['token']).exists():
            raise serializers.ValidationError('Invalid token.')

        return data


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def reset(self, validated_data):
        user = User.objects.get(reset_key=self.context['reset_key'])
        user.set_password(validated_data['password'])
        user.reset_key = None
        user.save()

    def validate(self, data):
        check_valid_password(data)
        self.check_valid_token()

        return data

    def check_valid_token(self):
        if not User.objects.filter(reset_key=self.context['reset_key']).exists():
            raise serializers.ValidationError('Token is not valid.')

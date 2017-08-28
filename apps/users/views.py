from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import (
    ForgotPasswordSerializer, SignUpSerializer,
    ConfirmAccountSerializer, ResetPasswordSerializer)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """
        ---
        serializer: AuthTokenSerializer
        :rtype: Response
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'pk': user.pk,
            'role': user.role,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })


class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        """
        ---
        request_serializer: ForgotPasswordSerializer
        :rtype: Response | JsonResponse
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.send_mail(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpAPIView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        """
        ---
        request_serializer: SignUpSerializer
        :rtype: Response | JsonResponse
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save_user(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, reset_key):
        """
        ---
        request_serializer: ResetPasswordSerializer
        :rtype: Response | JsonResponse
        """

        context = {
            'request': request,
            'reset_key': reset_key,
        }
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.reset(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmAccountAPIView(APIView):
    serializer_class = ConfirmAccountSerializer

    def post(self, request):
        """
        ---
        request_serializer: ConfirmAccountSerializer
        :rtype: Response | JsonResponse
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.confirm(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

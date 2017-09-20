from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import HasAPIAccess


class APIKEYView(APIView):
    permission_classes = (HasAPIAccess,)

    def get(self, request, format=None):
        return Response({
            'success': True,
        })

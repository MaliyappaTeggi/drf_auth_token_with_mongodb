from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework_simplejwt import authentication


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request):
        content = {'message': 'Hello, Maliyappa'}
        return Response(content)

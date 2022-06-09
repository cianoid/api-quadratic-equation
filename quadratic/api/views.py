from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import EquationSerializer


class SolutionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return Response(
            EquationSerializer(request.data).data, status=status.HTTP_200_OK)

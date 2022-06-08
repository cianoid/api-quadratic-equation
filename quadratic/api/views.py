from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import EquationSerializer


class SolutionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        required_fields = ['a', 'b', 'c']
        errors = []
        data = {}

        for key in required_fields:
            data[key] = request.data.get(key, None)
            if data[key] is None:
                errors.append(f'Не передан параметр {key}')

        if errors:
            return Response(
                {'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EquationSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)

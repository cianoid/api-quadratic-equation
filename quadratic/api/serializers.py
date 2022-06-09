from rest_framework import serializers

from core.calculate import calculate_equation


class EquationSerializer(serializers.Serializer):
    a = serializers.FloatField(required=True, write_only=True)
    b = serializers.FloatField(required=True, write_only=True)
    c = serializers.FloatField(required=True, write_only=True)

    def validate_a(self, a):
        if a == 0:
            raise serializers.ValidationError(
                'Параметр не может быть равен 0')

    def to_representation(self, instance):
        self.run_validation(instance)

        a = instance.pop('a')
        b = instance.pop('b')
        c = instance.pop('c')

        roots = calculate_equation(a, b, c)

        return {'roots_count': len(roots), 'roots': roots}

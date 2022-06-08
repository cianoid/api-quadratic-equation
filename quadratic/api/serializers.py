import math

from rest_framework import serializers


def calculate_equation(a, b, c):
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return {'roots_count': 0, 'roots': []}

    if discriminant == 0:
        roots = [- (b / (2 * a))]
    else:
        sqrt_ = math.sqrt(discriminant)
        roots = [
            (-b + sqrt_) / (2 * a),
            (-b - sqrt_) / (2 * a)
        ]

    roots = [0.0 if root == -0.0 else root for root in roots]

    return {'roots_count': len(roots), 'roots': roots}


class EquationSerializer(serializers.Serializer):
    a = serializers.FloatField(required=True, write_only=True)
    b = serializers.FloatField(required=True, write_only=True)
    c = serializers.FloatField(required=True, write_only=True)

    def to_representation(self, instance):
        a = instance.pop('a')

        if a == 0:
            raise serializers.ValidationError(
                {'errors': ['Параметр a не может быть равен 0']})

        b = instance.pop('b')
        c = instance.pop('c')

        instance = calculate_equation(a, b, c)

        return instance



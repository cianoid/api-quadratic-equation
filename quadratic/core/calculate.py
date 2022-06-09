import math


def calculate_equation(a, b, c):
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return []

    if discriminant == 0:
        roots = [- (b / (2 * a))]
    else:
        sqrt_ = math.sqrt(discriminant)
        roots = [
            (-b + sqrt_) / (2 * a),
            (-b - sqrt_) / (2 * a)
        ]

    return [0.0 if root == -0.0 else root for root in roots]

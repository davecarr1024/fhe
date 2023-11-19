import math
from unittest import TestCase
from fhe.math import mat2, rot2, vec2


class Mat2Test(TestCase):
    def test_identity(self):
        self.assertEqual(
            mat2.Mat2.identity() * vec2.Vec2(2, 3),
            vec2.Vec2(2, 3),
        )

    def test_translate(self):
        self.assertEqual(
            mat2.Mat2.translation(vec2.Vec2(1, 2)) * vec2.Vec2(3, 4),
            vec2.Vec2(4, 6),
        )

    def test_rotate(self):
        self.assertEqual(
            mat2.Mat2.rotation(rot2.Rot2(math.pi / 2)) * vec2.Vec2(1, 0),
            vec2.Vec2(0, 1),
        )
        self.assertEqual(
            mat2.Mat2.rotation(rot2.Rot2(-math.pi / 2)) * vec2.Vec2(1, 0),
            vec2.Vec2(0, -1),
        )

    def test_scale(self):
        self.assertEqual(
            mat2.Mat2.scale(vec2.Vec2(2, 3)) * vec2.Vec2(4, 5),
            vec2.Vec2(8, 15),
        )

    def test_inverse_translate(self):
        self.assertEqual(
            mat2.Mat2.translation(vec2.Vec2(1, 2)).inverse() * vec2.Vec2(3, 4),
            vec2.Vec2(2, 2),
        )

    def test_inverse_rotate(self):
        self.assertEqual(
            mat2.Mat2.rotation(rot2.Rot2(math.pi / 2)).inverse() * vec2.Vec2(1, 0),
            vec2.Vec2(0, -1),
        )

    def test_inverse_scale(self):
        self.assertEqual(
            mat2.Mat2.scale(vec2.Vec2(2, 3)).inverse() * vec2.Vec2(10, 30),
            vec2.Vec2(5, 10),
        )

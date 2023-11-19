import math
from unittest import TestCase
from fhe.math import rot2, vec2


class Rot2Test(TestCase):
    def test_ctor(self):
        self.assertEqual(rot2.Rot2(0), rot2.Rot2(0))
        self.assertEqual(rot2.Rot2(0), rot2.Rot2(math.pi * 2))
        self.assertEqual(rot2.Rot2(0), rot2.Rot2(math.pi * -2))

    def test_mul_vec(self) -> None:
        self.assertEqual(
            rot2.Rot2(math.pi) * vec2.Vec2(1, 0),
            vec2.Vec2(1, 0),
        )
        self.assertEqual(
            rot2.Rot2(math.pi / 2) * vec2.Vec2(1, 0),
            vec2.Vec2(0, 1),
        )

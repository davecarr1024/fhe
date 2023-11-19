from unittest import TestCase
from fhe.math import vec2


class Vec2Test(TestCase):
    def test_unpack(self) -> None:
        v = vec2.Vec2(1, 2)
        x, y = v
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 2)

    def test_mul(self) -> None:
        self.assertEqual(vec2.Vec2(1, 2) * 3, vec2.Vec2(3, 6))

    def test_div(self) -> None:
        self.assertEqual(vec2.Vec2(10, 20) / 5, vec2.Vec2(2, 4))

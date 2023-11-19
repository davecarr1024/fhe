from dataclasses import dataclass
import math
from typing import Iterable, Iterator, Sized, SupportsFloat, Union


@dataclass
class Vec2(
    Sized,
    Iterable[float],
):
    x: float
    y: float

    def __str__(self) -> str:
        return f"Vec2({self.x:.2f},{self.y:.2f})"

    def __eq__(self, rhs: object) -> bool:
        return (
            isinstance(rhs, Vec2)
            and math.isclose(self.x, rhs.x, abs_tol=1e-6)
            and math.isclose(self.y, rhs.y, abs_tol=1e-6)
        )

    def __len__(self) -> int:
        return 2

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def __neg__(self) -> "Vec2":
        return Vec2(-self.x, -self.y)

    def __add__(self, rhs: "Vec2") -> "Vec2":
        return Vec2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs: "Vec2") -> "Vec2":
        return Vec2(self.x - rhs.x, self.y - rhs.y)

    def __mul__(
        self,
        rhs: Union[
            "Vec2",
            SupportsFloat,
        ],
    ) -> "Vec2":
        match rhs:
            case SupportsFloat():
                rhs = float(rhs)
                return Vec2(self.x * rhs, self.y * rhs)
            case Vec2():
                return Vec2(self.x * rhs.x, self.y * rhs.y)
            case _:
                raise TypeError(type(rhs))

    def __truediv__(
        self,
        rhs: Union[
            "Vec2",
            SupportsFloat,
        ],
    ) -> "Vec2":
        match rhs:
            case SupportsFloat():
                rhs = float(rhs)
                return Vec2(self.x / rhs, self.y / rhs)
            case Vec2():
                return Vec2(self.x / rhs.x, self.y / rhs.y)
            case _:
                raise TypeError(type(rhs))

    def __matmul__(self, rhs: "Vec2") -> float:
        return self.x * rhs.x + self.y * rhs.y

    def norm(self) -> "Vec2":
        return self / self.length()

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def rot(self) -> "rot2.Rot2":
        return rot2.Rot2(math.atan2(self.y, self.x))


from fhe.math import rot2

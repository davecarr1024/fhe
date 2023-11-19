from dataclasses import dataclass
import math
from typing import SupportsFloat, Union, overload


@dataclass
class Rot2:
    th: float

    def __post_init__(self) -> None:
        self.th = math.fmod(self.th, math.pi)

    def __str__(self) -> str:
        return f"Rot2({self.th})"

    def __eq__(self, rhs: object) -> bool:
        return isinstance(rhs, Rot2) and math.isclose(self.th, rhs.th)

    def __abs__(self) -> "Rot2":
        return Rot2(math.fabs(self.th))

    def __add__(self, rhs: "Rot2") -> "Rot2":
        return Rot2(self.th + rhs.th)

    def __sub__(self, rhs: "Rot2") -> "Rot2":
        return Rot2(self.th - rhs.th)

    @overload
    def __mul__(self, rhs: SupportsFloat) -> "Rot2":
        ...

    @overload
    def __mul__(self, rhs: "vec2.Vec2") -> "vec2.Vec2":
        ...

    def __mul__(
        self, rhs: Union[SupportsFloat, "vec2.Vec2"]
    ) -> Union["Rot2", "vec2.Vec2"]:
        match rhs:
            case SupportsFloat():
                return Rot2(self.th * float(rhs))
            case vec2.Vec2():
                return (self + rhs.rot()).vec(rhs.length())
            case _:
                raise TypeError(type(rhs))

    def vec(self, l: float = 1) -> "vec2.Vec2":
        return vec2.Vec2(l * math.cos(self.th), l * math.sin(self.th))


from fhe.math import vec2

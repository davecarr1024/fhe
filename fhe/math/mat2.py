from dataclasses import dataclass
import math
from typing import Iterable, Iterator, MutableSequence, Sized, Union, overload


@dataclass
class Mat2(Sized, Iterable[float]):
    _vals: MutableSequence[float]

    def __post_init__(self) -> None:
        if len(self._vals) != 9:
            raise ValueError(self._vals)

    def __str__(self) -> str:
        return (
            "["
            + ",".join(
                f'[{",".join(f"{self[i,j]:.2f}" for j in range(3))}]' for i in range(3)
            )
            + "]"
        )

    def __len__(self) -> int:
        return 9

    def __iter__(self) -> Iterator[float]:
        return iter(self._vals)

    def __getitem__(self, index: int | tuple[int, int]) -> float:
        match index:
            case int():
                if index < 0 or index >= 9:
                    raise ValueError(index)
                return self._vals[index]
            case (i, j):
                if i < 0 or i >= 3 or j < 0 or j >= 3:
                    raise ValueError(index)
                return self._vals[i * 3 + j]
            case _:
                raise TypeError(index)

    def __setitem__(self, index: int | tuple[int, int], value: float) -> None:
        match index:
            case int():
                if index < 0 or index >= 9:
                    raise ValueError(index)
                self._vals[index] = value
            case (i, j):
                if i < 0 or i >= 3 or j < 0 or j >= 3:
                    raise ValueError(index)
                self._vals[i * 3 + j] = value
            case _:
                raise TypeError(index)

    @staticmethod
    def zero() -> "Mat2":
        return Mat2([0.0, 0, 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def identity() -> "Mat2":
        return Mat2([1.0, 0, 0, 0, 1, 0, 0, 0, 1])

    @staticmethod
    def translation(v: "vec2.Vec2") -> "Mat2":
        return Mat2([1, 0, v.x, 0, 1, v.y, 0, 0, 1])

    @staticmethod
    def rotation(r: "rot2.Rot2") -> "Mat2":
        sa = math.sin(-r.th)
        ca = math.cos(-r.th)
        return Mat2([ca, sa, 0, -sa, ca, 0, 0, 0, 1])

    @staticmethod
    def scale(v: "vec2.Vec2") -> "Mat2":
        return Mat2([v.x, 0, 0, 0, v.y, 0, 0, 0, 1])

    @overload
    def __mul__(self, rhs: "vec2.Vec2") -> "vec2.Vec2":
        ...

    @overload
    def __mul__(self, rhs: "Mat2") -> "Mat2":
        ...

    def __mul__(self, rhs: Union["vec2.Vec2", "Mat2"]) -> Union["vec2.Vec2", "Mat2"]:
        match rhs:
            case vec2.Vec2():
                return vec2.Vec2(
                    self[0] * rhs.x + self[1] * rhs.y + self[2],
                    self[3] * rhs.x + self[4] * rhs.y + self[5],
                )
            case Mat2():
                result = Mat2.zero()
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            result[i, j] += self[i, k] * rhs[k, j]
                return result
            case _:
                raise TypeError(type(rhs))

    def det(self) -> float:
        return (
            self[0] * (self[4] * self[8] - self[7] * self[5])
            - self[1] * (self[3] * self[8] - self[6] * self[5])
            + self[2] * (self[3] * self[7] - self[6] * self[4])
        )

    def inverse(self) -> "Mat2":
        d = self.det()
        if math.isclose(d, 0):
            raise ValueError(d)
        return Mat2(
            [
                (self[4] * self[8] - self[5] * self[7]) / d,
                -(self[1] * self[8] - self[7] * self[2]) / d,
                (self[1] * self[5] - self[4] * self[2]) / d,
                -(self[3] * self[8] - self[5] * self[6]) / d,
                (self[0] * self[8] - self[6] * self[2]) / d,
                -(self[0] * self[5] - self[3] * self[2]) / d,
                (self[3] * self[7] - self[6] * self[4]) / d,
                -(self[0] * self[7] - self[6] * self[1]) / d,
                (self[0] * self[4] - self[1] * self[3]) / d,
            ]
        )


from fhe.math import vec2, rot2

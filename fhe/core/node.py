from dataclasses import dataclass, field
from typing import (
    Iterable,
    Iterator,
    MutableSet,
    Optional,
    Set,
    Sized,
    Type,
)


@dataclass
class Node(
    Sized,
    Iterable["Node"],
):
    _parent: Optional["Node"] = None
    _children: MutableSet["Node"] = field(default_factory=set)

    @property
    def parent(self) -> Optional["Node"]:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional["Node"]) -> None:
        if self._parent is not None:
            self._parent._children.remove(self)
        self._parent = parent
        if self._parent is not None:
            self._parent._children.add(self)

    @property
    def children(self) -> Set["Node"]:
        return set(self._children)

    @children.setter
    def children(self, children: MutableSet["Node"]) -> None:
        for child in self._children:
            child.parent = None
        self._children = children
        for child in self._children:
            child.parent = self

    def add_child(self, child: "Node") -> None:
        child.parent = self

    def remove_child(self, child: "Node") -> None:
        child.parent = None

    def __len__(self) -> int:
        return len(self._children)

    def __iter__(self) -> Iterator["Node"]:
        return iter(self._children)

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, final

_Node = TypeVar("_Node", bound="node.Node")


class Visitor(ABC, Generic[_Node]):
    @final
    def visit(self, node: "node.Node") -> None:
        if isinstance(node, _Node):
            self._visit(node)

    @abstractmethod
    def _visit(self, node: _Node) -> None:
        ...


from fhe.core import node

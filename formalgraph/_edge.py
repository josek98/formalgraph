from abc import ABC
from typing import Hashable

Node = Hashable


class Edge:

    def __init__(
        self,
        source: Node,
        target: Node,
        directed: bool = False,
        weight: float | None = None,
    ) -> None:
        self._source = source
        self._target = target
        self._directed = directed
        self._weight = weight

        if not directed and weight is not None:
            raise ValueError("Undirected edges cannot be weighted")

    @property
    def is_directed(self) -> bool:
        return self._directed

    @property
    def is_weighted(self) -> bool:
        return self._weight is not None

    @property
    def source(self) -> Node:
        if not self._directed:
            raise ValueError("This edge is not directed")

        return self._source

    @property
    def target(self) -> Node:
        if not self._directed:
            raise ValueError("This edge is not directed")

        return self._target

    @property
    def weight(self) -> float:
        if self._weight is None:
            raise ValueError("This edge is not weighted")

        return self._weight

    def __hash__(self):
        return hash((self._source, self._target, self._directed, self._weight))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False

        if self._directed != other._directed:
            return False

        if self._weight != other._weight:
            return False

        if self._directed:
            return self._source == other._source and self._target == other._target

        return False
    
    @classmethod
    def from_tuple(cls, edge: tuple[Node, Node] | tuple[Node, Node, float]) -> "Edge":
        if len(edge) == 2:
            return cls(edge[0], edge[1], directed=True)
        if len(edge) == 3:
            return cls(edge[0], edge[1], directed=True, weight=edge[2])
        raise ValueError("Invalid edge tuple")
    
    @classmethod
    def from_set(cls, edge: set[Node]) -> Node:
        if len(edge) == 1: 
            node = list(edge)[0]
            return cls(node, node, directed=False)
        if len(edge) == 2:
            node1, node2 = list(edge)
            return cls(node1, node2, directed=False)
        
        raise ValueError("Invalid edge set")
    
    def __repr__(self):
        if not self._directed:
            return f"{self._source} -- {self._target}"
        
        
        if self._source == self._target:
            if self._weight is None:
                return f"{self._source} <-> {self._target}"
            
            return f"{self._source} <-> {self._target} ({self._weight})"
            
        else:
            if self._weight is None:
                return f"{self._source} -> {self._target}"
        
            return f"{self._source} -> {self._target} ({self._weight})"

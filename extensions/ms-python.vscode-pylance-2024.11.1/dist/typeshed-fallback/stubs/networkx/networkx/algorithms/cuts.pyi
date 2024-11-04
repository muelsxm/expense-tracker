from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def cut_size(G, S, T: Incomplete | None = None, weight: Incomplete | None = None): ...
@_dispatchable
def volume(G, S, weight: Incomplete | None = None): ...
@_dispatchable
def normalized_cut_size(G, S, T: Incomplete | None = None, weight: Incomplete | None = None): ...
@_dispatchable
def conductance(G, S, T: Incomplete | None = None, weight: Incomplete | None = None): ...
@_dispatchable
def edge_expansion(G, S, T: Incomplete | None = None, weight: Incomplete | None = None): ...
@_dispatchable
def mixing_expansion(G, S, T: Incomplete | None = None, weight: Incomplete | None = None): ...
@_dispatchable
def node_expansion(G, S): ...
@_dispatchable
def boundary_expansion(G, S): ...
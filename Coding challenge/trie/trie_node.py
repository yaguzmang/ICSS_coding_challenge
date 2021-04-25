
class TrieNode:
    """
    A class used to represent a Trie node

    ...

    Attributes
    ----------
    name : str
        The value of the node ('root' or the digits).
    children : dict
        The pointers the nodes' children -> { name : TrieNode }.
    prices : dict
        The prices for prefixes ending in this node -> { operator_name : price }.
        If a node does not have any prices, it means that there are no operators
        with a prefix ending at that node(digit).

    """
    def __init__(self):
        self.value = None
        self.children = {}
        self.prices = {}

    def __repr__(self):
        children_string = str(self.children.keys())
        return f"Current: {self.value}. Children: {children_string}. Prices: {str(self.prices)}"
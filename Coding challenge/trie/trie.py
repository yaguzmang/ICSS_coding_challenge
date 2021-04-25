from .trie_node import TrieNode

class Trie:
    """
    A class used to represent a Prefix Trie

    ...

    Attributes
    ----------
    root : TrieNode
        The root node of the trie.

    """
    def __init__(self):
        self.root = TrieNode()
        self.root.value = 'root'


    def insert(self, operator_name: str, phone_prefix: str, price: float) -> None:
        """Inserts the given telephone prefix into the Trie."""
        try:
            if not phone_prefix.isdigit():
                raise ValueError("The phone prefix contains non-digit chars")
            if not isinstance(price, float):
                raise ValueError("The price is not a number")
            node = self.root
            for char in phone_prefix:
                if char not in node.children:
                    node.children[char] = TrieNode()
                    node.children[char].value = char
                node = node.children[char]
            node.prices[operator_name] = price

        except Exception as err:
            print(err)
            raise # raise for the unit tests

    def find_cheapest(self, phone_number: str) -> (float, str, str):
        """
        Returns the cheapest price, prefix and operator for the given 
        telephone number by traversing the Trie and finding the best operator.
        """
        try:
            if not phone_number.isdigit():
                raise ValueError("The phone number contains non-digit chars")
            # valid prefixes per operator, having that the longest must be used
            valid_options = {} 
            option = (None, None, None) # (price, prefix, operator)
            current_prefix = [] # a list is used to efficiently append the chars
            node = self.root
            for char in phone_number:
                # if there are no more prefixes that match the phone number
                if char not in node.children: 
                    break
                current_prefix.append(char)
                node = node.children[char]
                # update the prices dict with the longest matching prefix price
                for operator in node.prices.keys():
                    option = (node.prices[operator], current_prefix[:], operator)
                    valid_options[operator] = option

            cheapest_option = (float('inf'), None, None) # (price, prefix, operator)

            for operator in valid_options.keys():
                option = valid_options[operator]
                if option[0] < cheapest_option[0]: 
                    cheapest_option = option
            # Join the prefix char list (tuple inmutable)
            if cheapest_option[2] is not None:
                cheapest_option = (cheapest_option[0],''.join(cheapest_option[1]), cheapest_option[2])
            return cheapest_option

        except Exception as err:
            raise

    def search(self, phone_prefix: str) -> bool:
        """
        Traverses the Trie given the phone prefix. Returns the prices if the prefix
        is in the Trie and False if it is not.
        """
        try:
            if not phone_prefix.isdigit():
                raise ValueError("The phone prefix contains non-digit chars")
            node = self.root
            for char in phone_prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            if not node.prices:
                return False
            return node.prices
        except Exception as err:
            print(err)
            raise # raise for the unit tests
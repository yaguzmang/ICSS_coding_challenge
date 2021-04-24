import unittest
from trie.trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        # data from the example
        self.operators_data = {
            'A': [['1', 0.9], ['268', 5.1], 
                  ['46', 0.17], ['4620', 0.0], 
                  ['468', 0.15], ['4631', 0.15], 
                  ['4673', 0.9], ['46732', 1.1]], 
            'B': [['1', 0.92], ['44', 0.5], 
                  ['46', 0.2], ['467', 1.0], 
                  ['48', 1.2]]}

    def test_insert_datatype(self):
        """Insertion datatype tests"""

        trie = Trie()

        with self.assertRaises(ValueError):
            trie.insert('A','+123',1.1)
        with self.assertRaises(ValueError):
            trie.insert('A','-123',1.1)
        with self.assertRaises(ValueError):
            trie.insert('A','.123',1.1)
        with self.assertRaises(ValueError):
            trie.insert('A','123','1.1')
        with self.assertRaises(ValueError):
            trie.insert('A','123','1.1')

    def test_insert(self):
        """Insertion tests"""

        trie = Trie()

        trie.insert('A','123',1.1)
        self.assertFalse(trie.search('12'))
        self.assertFalse(trie.search('1234'))
        self.assertDictEqual(trie.search('123'), {'A':1.1})
        trie.insert('B','123',5.5)
        self.assertDictEqual(trie.search('123'), {'A':1.1, 'B':5.5})
        trie.insert('B','123',5.0) # Updates the price
        self.assertDictEqual(trie.search('123'), {'A':1.1, 'B':5.0})

    def test_insert_stored_data(self):
        """Insertion tests with the example operators data"""
        # Reasoning behind some test cases is included in comments below
        trie = Trie()

        for operator in self.operators_data.keys():
            for item in self.operators_data[operator]:
                telephone_prefix = item[0]
                price = item[1]
                operator_name = str(operator)
                trie.insert(operator_name,telephone_prefix,price)

        self.assertFalse(trie.search('4')) # Many prefixes starting with 4, but 4 itself is not a prefix
        self.assertFalse(trie.search('0')) # Not included
        self.assertFalse(trie.search('463')) # 4631 is included but 463 is not
        self.assertDictEqual(trie.search('46'), {'A':0.17, 'B':0.2}) # 2 Operators with the same prefix
        self.assertDictEqual(trie.search('1'), {'A':0.9, 'B':0.92}) # 2 Operators with the same prefix
        self.assertDictEqual(trie.search('467'), {'B':1.0}) # 467 is in some prefixes of A, but 467 itself is not a prefix
        self.assertDictEqual(trie.search('46732'), {'A':1.1}) # Deep prefix. Only in A
        self.assertDictEqual(trie.search('268'), {'A':5.1}) # Only prefix starting by 2

    def test_find_cheapest_datatype(self):
        """Find-cheapest datatype tests"""
        trie = Trie()

        trie.insert('A','123',1.1)
        self.assertListEqual(list(trie.find_cheapest('123456789')), [1.1, '123', 'A'])
        with self.assertRaises(ValueError):
            trie.find_cheapest('+1238888')
        with self.assertRaises(ValueError):
            trie.find_cheapest('-1238888')
        with self.assertRaises(ValueError):
            trie.find_cheapest('12.38888')
        with self.assertRaises(ValueError):
            trie.find_cheapest('4638888.')
        with self.assertRaises(ValueError):
            trie.find_cheapest('123089.')
        

    def test_find_cheapest_new_data(self):
        """Find-cheapest tests with different operators data"""
        # Reasoning behind some test cases is included in comments below
        new_operators_data = {
            'A': [['123', 0.5], ['456', 2.0], 
                  ['1234', 0.2], ['4567', 8.0]], 
            'B': [['123', 0.4], ['789', 0.5]]}

        trie = Trie()

        for operator in new_operators_data.keys():
            for item in new_operators_data[operator]:
                telephone_prefix = item[0]
                price = item[1]
                operator_name = str(operator)
                trie.insert(operator_name,telephone_prefix,price)

        self.assertListEqual(list(trie.find_cheapest('123999')), [0.4, '123', 'B']) # Included in A but cheaper in B
        self.assertListEqual(list(trie.find_cheapest('123499')), [0.2, '1234', 'A']) # Longest matching in A is cheaper
        self.assertListEqual(list(trie.find_cheapest('456799')), [8.0, '4567', 'A']) # 456 cheaper but 4567 is the longest matching
        self.assertListEqual(list(trie.find_cheapest('987054')), [float('inf'), None, None]) # No operator supports it
        self.assertListEqual(list(trie.find_cheapest('789001')), [0.5, '789', 'B']) # Only B supports it
        
    def test_find_cheapest_stored_data(self):
        """Find-cheapest tests with different operators data"""
        # Reasoning behind some test cases is included in comments below
        trie = Trie()

        for operator in self.operators_data.keys():
            for item in self.operators_data[operator]:
                telephone_prefix = item[0]
                price = item[1]
                operator_name = str(operator)
                trie.insert(operator_name,telephone_prefix,price)

        self.assertListEqual(list(trie.find_cheapest('460000')), [0.17, '46', 'A']) # 2 Operators with the same prefix
        self.assertListEqual(list(trie.find_cheapest('199999')), [0.9, '1', 'A']) # 2 Operators with the same prefix
        self.assertListEqual(list(trie.find_cheapest('468000')), [0.15, '468', 'A']) # 468 in A vs 46 in B
        self.assertListEqual(list(trie.find_cheapest('548970')), [float('inf'), None, None]) # No operator supports it
        self.assertListEqual(list(trie.find_cheapest('440000')), [0.5, '44', 'B']) # Only B supports it
        self.assertListEqual(list(trie.find_cheapest('467320')), [1.0, '467', 'B']) # Longest match on A results on B cheaper
        self.assertListEqual(list(trie.find_cheapest('467300')), [0.9, '4673', 'A']) # 4673 in A vs 467 in B 

if __name__ == '__main__':
    unittest.main()
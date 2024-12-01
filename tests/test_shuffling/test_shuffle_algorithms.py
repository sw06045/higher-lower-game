import unittest
from src.shuffling import shuffle_algorithms

class TestShuffleAlgorithms(unittest.TestCase):
    def setUp(self):
        self.orig_list = list(range(1, 53))

    def test_do_overhand(self):
        shuffled_list = shuffle_algorithms.do_overhand(self.orig_list.copy(), num_shuffles=1)
        self.assertNotEqual(shuffled_list, self.orig_list)

    def test_do_pile(self):
        shuffled_list = shuffle_algorithms.do_pile(self.orig_list.copy(), max_num_piles=4, num_shuffles=1)
        self.assertNotEqual(shuffled_list, self.orig_list)

    def test_do_52_pickup(self):
        shuffled_list = shuffle_algorithms.do_52_pickup(self.orig_list.copy(), num_pickups=1)
        self.assertNotEqual(shuffled_list, self.orig_list)

    def test_do_mongean(self):
        shuffled_list = shuffle_algorithms.do_mongean(self.orig_list.copy(), num_shuffles=1)
        self.assertNotEqual(shuffled_list, self.orig_list)

if __name__ == "__main__":
    unittest.main()
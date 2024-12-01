import random
from abc import ABC, abstractmethod
import shuffling.shuffle_algorithms as shuffle_algorithms

class ShuffleStrategy(ABC):
    @abstractmethod
    def shuffle(self, cards, seed=None):
        pass

class OverhandShuffle(ShuffleStrategy):
    def shuffle(self, cards, seed=None):
        if seed is not None:
            random.seed(seed)
        num_shuffles = random.randint(500, 999)
        return shuffle_algorithms.do_overhand(cards, num_shuffles)

class PileShuffle(ShuffleStrategy):
    def shuffle(self, cards, seed=None):
        if seed is not None:
            random.seed(seed)
        max_num_piles = random.randint(5, 10)
        num_shuffles = random.randint(500, 999)
        return shuffle_algorithms.do_pile(cards, max_num_piles, num_shuffles)

class PickupShuffle(ShuffleStrategy):
    def shuffle(self, cards, seed=None):
        if seed is not None:
            random.seed(seed)
        num_pickups = random.randint(1, 50)
        return shuffle_algorithms.do_52_pickup(cards, num_pickups)

class MongeanShuffle(ShuffleStrategy):
    def shuffle(self, cards, seed=None):
        if seed is not None:
            random.seed(seed)
        num_shuffles = random.randint(500, 999)
        return shuffle_algorithms.do_mongean(cards, num_shuffles)

class DefaultShuffle(ShuffleStrategy):
    def shuffle(self, cards, seed=None):
        if seed is not None:
            random.seed(seed)
        random.shuffle(cards)
        return cards
import random
import time
from abc import ABC, abstractmethod


def do_overhand(orig_list, num_shuffles):
    """
    Perform an overhand shuffle on a list a specified number of times.
    Args:
        orig_list (list): The original list to be shuffled.
        num_shuffles (int): The number of times to shuffle the list.
    Returns:
        list: The shuffled list after the specified number of shuffles.
    
    The overhand shuffle is a common shuffling technique where a small number of items 
    are taken from the original list and placed into the shuffled list. 
    This process is repeated until the entire list has been shuffled. The function 
    recursively shuffles the list the specified number of times.
    """
    length = len(orig_list)
    shuffled_list = [None] * length

    # Progress reverse through shuffled list
    shuffled_index = length - 1

    # Progress forwards through original list
    original_index = 0

    # Make sure we don't run off the end of the original list
    while original_index < length:
        # Get random number of items (min of 1)
        # To ensure a good shuffle, should be a small number
        # Set max number of cards that can be shuffled at once to 5
        num_items = random.randint(1, 5)

        remaining_items = length - original_index
        if num_items > remaining_items:
            num_items = remaining_items

        for i in range(num_items):
            # Add item to new shuffled_list from the orig_list
            shuffled_list[shuffled_index - (num_items - (i + 1))] = orig_list[original_index + i]

        # Move progress identifiers to next position
        shuffled_index -= num_items
        original_index += num_items

    # Recursively shuffle the desired amount
    num_shuffles -= 1
    if num_shuffles > 0:
        shuffled_list = do_overhand(shuffled_list, num_shuffles)

    return shuffled_list


def do_pile(orig_list, max_num_piles, num_shuffles):
    """
    Perform a pile shuffle on a list of items.
    Args:
        orig_list (list): The original list of items to be shuffled.
        num_piles (int): The number of piles to use for the shuffle.
        num_shuffles (int): The number of times to recursively shuffle the list.
    Returns:
        list: The shuffled list of items.
    The function simulates a pile shuffle by distributing the items into a specified number of piles,
    reversing each pile, and then concatenating the piles back together. This process is repeated
    recursively for the specified number of shuffles.
    """

    length = len(orig_list)
    
    # Initialise empty list to return
    shuffled_list = []

    # Initialise piles
    num_piles = random.randint(3, max_num_piles)
    piles_array = [[] for _ in range(num_piles)]

    # Deal items into respective piles
    for i in range(length):
        pile = i % num_piles
        piles_array[pile].append(orig_list[i])

    # Build the final shuffled list by concatenating all piles
    for pile in piles_array:
        shuffled_list.extend(pile)

    # Recursively shuffle the desired amount
    num_shuffles -= 1
    if num_shuffles > 0:
        shuffled_list = do_pile(shuffled_list, num_piles, num_shuffles)

    return shuffled_list


def do_52_pickup(orig_list, num_pickups):
    """
    Simulates the "52 pickup" card game by randomly shuffling a list of items.
    Args:
        orig_list (list): The original list of items to be shuffled.
        num_pickups (int): The number of times to repeat the pickup process.
    Returns:
        list: The shuffled list after performing the specified number of pickups.

        This function modifies the original list by popping elements from it.
    """
    shuffled_list = []
    # Simulate picking up the cards in random order
    while orig_list:
        index = random.randint(0, len(orig_list) - 1)
        shuffled_list.append(orig_list.pop(index))
    
    # Simulate doing 52 pickup a number of times
    num_pickups -= 1
    if num_pickups > 0:
        shuffled_list = do_52_pickup(shuffled_list, num_pickups)
    
    return shuffled_list


def do_mongean(orig_list, num_shuffles):
    """
    Perform the Mongean shuffle on a list a specified number of times.
    The Mongean shuffle is a specific way of shuffling a list where items are alternately placed
    at the front and back of the shuffled list.
    Args:
        orig_list (list): The original list to be shuffled.
        num_shuffles (int): The number of times to perform the shuffle.
    Returns:
        list: The shuffled list after the specified number of shuffles.
    """

    length = len(orig_list)
    shuffled_list = [None] * length

    current = length // 2
    for i in range(length):
        shuffled_list[current] = orig_list[i]

        # Calculate position of next item
        if i % 2:  # even (back)
            current += (i + 1)
        else:  # odd (front)
            current -= (i + 1)

    # Recursively shuffle the desired amount
    num_shuffles -= 1
    if num_shuffles > 0:
        shuffled_list = do_mongean(shuffled_list, num_shuffles)

    return shuffled_list


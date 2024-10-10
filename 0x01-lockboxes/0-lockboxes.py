#!/usr/bin/python3
"""
@Author :ZaneleYenziwe <https://github.com/ZaneleYenziwe/alx-interview.git>

Determines if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list represents a box.
                              The numbers in the inner list are keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Number of boxes
    n = len(boxes)
    
    # Initialize a set to keep track of opened boxes
    opened = set([0])  # Box 0 is initially open
    
    # Initialize a queue with the keys from box 0
    keys_to_try = boxes[0]
    
    # While there are still keys to try
    while keys_to_try:
        # Get the next key
        key = keys_to_try.pop(0)
        
        # If the key corresponds to a box that hasn't been opened yet
        if key not in opened and key < n:
            # Open the box and add its keys to the queue
            opened.add(key)
            keys_to_try.extend(boxes[key])
    
    # Return True if all boxes have been opened, False otherwise
    return len(opened) == n


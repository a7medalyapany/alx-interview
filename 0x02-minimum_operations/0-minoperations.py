#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed.

    """
    # Your code goes here
    pass

if __name__ == "__main__":
    # Test cases
    n1 = 4
    print("Min number of operations to reach {} characters: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min number of operations to reach {} characters: {}".format(n2, minOperations(n2)))

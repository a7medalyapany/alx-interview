#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    Args:
        coins: list of integers representing coin values
        total: total amount of change needed
    Return: 0 if total is 0 or less
            -1 if total cannot be met by any number of coins
            fewest number of coins to meet total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:
            num_coins += total // coin
            total = total % coin
    if total != 0:
        return -1
    return num_coins
    

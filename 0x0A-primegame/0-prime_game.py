#!/usr/bin/python3
"""
This module defines the isWinner function to determine the winner
of a prime number game played between Maria and Ben.
"""

def sieve_of_eratosthenes(n):
    """Generate a list of primes and a sieve up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    
    for start in range(2, int(n ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False
                
    primes = [i for i in range(n + 1) if sieve[i]]
    return primes, sieve

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    x: the number of rounds.
    nums: array of integers representing the numbers for each round.
    Returns: the name of the player with the most wins or None if a tie.
    """
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    primes, sieve = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = 0
        for p in primes:
            if p > n:
                break
            prime_count += 1
        
        # Maria wins if prime_count is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

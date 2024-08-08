def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False
                
    primes = [i for i in range(n + 1) if sieve[i]]
    return primes, sieve

def isWinner(x, nums):
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


if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

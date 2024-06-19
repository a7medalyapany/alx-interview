def makeChange(coins, total):
    if total < 0:
        return -1
    
    # Initialize dp array with infinity (float('inf'))
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make amount 0
    
    # Calculate minimum coins required for each amount from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1

# Testing the function with given examples
print(makeChange([1, 2, 25], 37))   # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1

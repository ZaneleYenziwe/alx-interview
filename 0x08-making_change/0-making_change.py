#!/usr/bin/python3
"""
Make Change
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    Return the fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


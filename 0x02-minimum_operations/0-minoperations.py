#!/usr/bin/python
def minOperations(n):
    """
    Calculate the minimum number of operations (Copy All and Paste)
    needed to result in exactly n 'H' characters in a text file.

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations. If n is impossible to achieve, return 0.
    """
    if n < 1:
        return 0

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible operations (i.e., Paste i times)
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j + 1)
                break

    return dp[n]


#!/usr/bin/python3
"""
Prime Game
"""

def sieve(n):
    """Returns a list of prime numbers up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [p for p in range(n + 1) if is_prime[p]]

def play_game(n, primes):
    """Simulates the game and returns the winner for a given n."""
    set_nums = set(range(1, n + 1))
    turn = 0  # Maria starts first
    while True:
        prime_picked = False
        for prime in primes:
            if prime in set_nums:
                prime_picked = True
                set_nums -= set(range(prime, n + 1, prime))
                break
        if not prime_picked:
            return "Maria" if turn % 2 == 1 else "Ben"
        turn += 1

def isWinner(x, nums):
    """Determines the winner of each game."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print(isWinner(3, [4, 5, 1]))  # Output: Ben


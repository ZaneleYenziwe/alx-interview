def isWinner(x, nums):
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while p ** 2 <= n:
            if is_prime[p]:
                for i in range(p ** 2, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    def play_game(n):
        primes = sieve(n)
        primes_set = set(primes)
        multiples_removed = [0] * (n + 1)
        for prime in primes:
            for multiple in range(prime, n + 1, prime):
                multiples_removed[multiple] = 1
        return sum(multiples_removed) % 2 == 0

    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if play_game(num):
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

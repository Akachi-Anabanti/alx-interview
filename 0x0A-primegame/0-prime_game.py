#!/usr/bin/python3
'''A script that defines a prime number'''


def seive_of_eratosthenes(n):
    """used to seive the prime numbers of n"""
    # Create a boolean array
    # "prime[0..n]" and initialize all to true
    # A value in prime[i] will fina,y be false if i is not
    # a prime, else true

    prime = [True] * (n + 1)

    p = 2

    while (p * p <= n):
        if prime[p]:
            # set the multiples of p to false
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [num for num in range(2, n + 1) if prime[num]]


def isWinner(x, nums):
    """
    Args:
        nums (list): List of numbers
        x (int): The number of rounds
    """
    marias_score = 0
    bens_score = 0

    for i in range(x):
        if i > len(nums) - 1:
            break
        n = nums[i]
        prime = seive_of_eratosthenes(n)

        if len(prime) == 0:
            bens_score += 1
            continue

        maria_picks_count = 0
        ben_picks_count = 0

        for j in prime:
            if (i + 1) % 2 == 1:  # Marias turn
                maria_picks_count += 1
            else:
                ben_picks_count += 1  # Bens turn
        if maria_picks_count > ben_picks_count:
            marias_score += 1
        if ben_picks_count > maria_picks_count:
            bens_score += 1

    if marias_score > bens_score:
        return 'Maria'
    if bens_score > marias_score:
        return 'Ben'
    return None

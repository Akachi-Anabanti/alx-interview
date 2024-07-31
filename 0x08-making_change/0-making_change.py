#!/usr/bin/python3
'''Coin change problem solution with Dynamic programming'''


def makeChange(coins, total):
    """A function that makes change for a total sum
    with a list of coins
    args:
        coins (list[int]): A list of subdivision of coins with
                            infinte supply
        total (int): The total sum to be gotten
    return:
        0: if total is 0 or less
        -1: if total cannot be met by any number of coins you have
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            break
    if total > 0:
        return -1
    return count

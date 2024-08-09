#!/usr/bin/python3

import unittest

sieve_of_eratosthenes = __import__('0-prime_game').sieve_of_eratosthenes


isWinner = __import__('0-prime_game').isWinner

class TestPrimeGame(unittest.TestCase):

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(sieve_of_eratosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(sieve_of_eratosthenes(2), [2])
        self.assertEqual(sieve_of_eratosthenes(1), [])
        self.assertEqual(sieve_of_eratosthenes(0), [])

    def test_isWinner_maria_wins(self):
        self.assertEqual(isWinner(3, [4, 5, 1]), 'Maria')
        self.assertEqual(isWinner(5, [2, 5, 1, 4, 3]), 'Maria')

    def test_isWinner_ben_wins(self):
        self.assertEqual(isWinner(3, [5, 5, 5]), 'Ben')
        self.assertEqual(isWinner(4, [1, 2, 3, 4]), 'Ben')

    def test_isWinner_tie(self):
        self.assertIsNone(isWinner(3, [2, 3, 4]))
        self.assertIsNone(isWinner(2, [2, 2]))

    def test_isWinner_empty_list(self):
        self.assertIsNone(isWinner(3, []))

    def test_isWinner_x_greater_than_nums(self):
        self.assertEqual(isWinner(5, [2, 3]), 'Maria')

    def test_isWinner_large_numbers(self):
        self.assertEqual(isWinner(2, [10000, 10001]), 'Ben')

    def test_isWinner_all_primes(self):
        self.assertEqual(isWinner(4, [2, 3, 5, 7]), 'Maria')

    def test_isWinner_no_primes(self):
        self.assertEqual(isWinner(3, [1, 4, 6]), 'Ben')

    def test_isWinner_single_round(self):
        self.assertEqual(isWinner(1, [2]), 'Maria')
        self.assertEqual(isWinner(1, [4]), 'Ben')

    def test_isWinner_alternating_primes_non_primes(self):
        self.assertIsNone(isWinner(6, [2, 4, 3, 6, 5, 8]))

if __name__ == '__main__':
    unittest.main()

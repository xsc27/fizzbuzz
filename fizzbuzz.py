#!/usr/bin/env python3
from typing import List
import argparse


def check_fizz(n: int) -> str:
    return "fizz" if n % 3 == 0 else ""


def check_buzz(n: int) -> str:
    return "buzz" if n % 5 == 0 else ""


def check_fizzbuzz(n: int) -> str:
    x = check_fizz(n) + check_buzz(n)
    return str(n) if x == "" else x


def fizzbuzz(n: int) -> List[str]:
    return [check_fizzbuzz(i) for i in range(1, n + 1)]


def fizzbuzz_cli():
    fizzbuzz_parser = argparse.ArgumentParser(description="Fizzbuzz!!!")
    fizzbuzz_parser.add_argument('number', type=str, help="Input number to print up to")
    fizzbuzz_args = fizzbuzz_parser.parse_args()
    n = fizzbuzz_args.number
    print(fizzbuzz(int(n)))


def test_check_fizz():
    n = 3
    result = check_fizz(n)
    assert result == "fizz"


def test_check_buzz():
    n = 5
    result = check_buzz(n)
    assert result == "buzz"


def test_check_fizzbuzz():
    n = 15
    result = check_fizzbuzz(n)
    assert result == "fizzbuzz"


def test_check_fizzbuzz_001():
    """Given when n is NOT a multiple of 3 and 5"""
    n = 1
    result = check_fizzbuzz(n)
    assert result == "1"


def test_fizzbuzz():
    n = 15
    result = fizzbuzz(n)
    assert result == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7',
                      '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']


def main():
    n = input("Please enter a number: ")
    print(fizzbuzz(int(n)))


if __name__ == "__main__":
    main()

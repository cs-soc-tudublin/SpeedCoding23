"""
Given a string, test if it is a palindrome or not
"""


def is_palindrome(data: str) -> bool:
    left = 0
    right = 1

    while left < len(data) / 2:
        print(data[left], data[-right])
        if data[left] != data[-right]:
            return False
        left += 1
        right += 1
    return True

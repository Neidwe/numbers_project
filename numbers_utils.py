number = int(input("Введите число >>> "))
def digit_sum(number: int) -> int:
    return sum(int(d) for d in str(abs(number)))
def count_digits(number):
    return len(str(number))
def max_digits(number):
    return max(int(d) for d in str(abs(number)))
def min_digits(number):
    return min(int(d) for d in str(abs(number)))
def is_even(number):
    return number % 2 == 0
def multiply_digits(number):
    result = 1
    for d in str(abs(number)):
        result *= int(d)
    return result
def reverse_number(number):
    reversed_str = str(abs(number))[::-1]
    return int(reversed_str)
def is_palindrome(number):
    s = str(abs(number))
    return s == s[::-1]
def count_even_digits(number):
    return sum(1 for d in str(abs(number)) if int(d) % 2 == 0)
def count_odd_digits(number):
    return sum(1 for d in str(abs(number)) if int(d) % 2 != 0)
def first_digit(number):
    return int(str(abs(number))[0])
def last_digit(number):
    return int(str(abs(number))[-1])
def sum_even_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)
def  sum_odd_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 != 0)
def square_number(number):
    return int(str(abs(number))) ** 2
def cube_number(number):
    return int(str(abs(number))) ** 3
def average_digit(number):
    digits = [int(d) for d in str(abs(number))]
    return sum(digits) / len(digits)
def is_positive(number):
    return number > 0
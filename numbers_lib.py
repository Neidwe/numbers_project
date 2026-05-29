def digit_sum(number: int) -> int:
    return sum(int(d) for d in str(abs(number)))
def count_digits(number):
    return len(str(number))
def max_digits(number):
    return max(int(d) for d in str(abs(number)))
def min_digits(number):
    return min(int(d) for d in str(abs(number)))

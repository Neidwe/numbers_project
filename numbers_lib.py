def digit_sum(number: int) -> int:
    return sum(int(d) for d in str(abs(number)))

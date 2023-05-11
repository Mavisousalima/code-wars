

def smallest_and_largest(numbers):
    numbers_sorted = sorted(numbers)

    return f"{numbers_sorted[0]} and {numbers_sorted[-1]}"


assert smallest_and_largest([3, 2, 5]) == "2 and 5"

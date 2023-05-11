def check_sum(numbers, target):
    complements = {}
    for number in numbers:
        if number in complements:
            return f"{number} and {complements[number]}"
        complements[target - number] = number
    return False


assert check_sum([14, 13, 6, 7, 8, 10, 1, 2], 16) == "10 and 6"

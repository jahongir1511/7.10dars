#misol linki   https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

def remove_smallest(numbers):
    if not numbers:
        return []

    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i

    result = numbers[:]

    result.pop(min_index)

    return result


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))

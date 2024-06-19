#misol linki   https://www.codewars.com/kata/5ac5e9aa3853da25d9000102/train/python

def or_arrays(arr1, arr2, default=0):
    min_length = min(len(arr1), len(arr2))

    result = []
    for i in range(min_length):
        result.append(arr1[i] | arr2[i])

    if len(arr1) > min_length:
        result.extend(arr1[min_length:])
    elif len(arr2) > min_length:
        result.extend(arr2[min_length:])

    return result


print(or_arrays([1, 2, 3], [1, 2, 3]))
print(or_arrays([1, 2, 3], [4, 5, 6]))
print(or_arrays([1, 2, 3], [1, 2]))
print(or_arrays([1, 2], [1, 2, 3]))
print(or_arrays([1, 2, 3], [1, 2, 3], 3))

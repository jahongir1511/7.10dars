#misol linki   https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python


def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        first_part = ' '.join(arr[:i])
        second_part = ' '.join(arr[i:])
        result.append((first_part, second_part))
    return result

print(partlist(["az", "toto", "picaro", "zone", "kiwi"]))

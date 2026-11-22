n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists):
    result = []
    for lst in lists:
        for item in lst:
            result.append(item)
    return result


print(flatten(n))

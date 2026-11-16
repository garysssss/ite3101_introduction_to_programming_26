n = [3, 5, 7]


def double_list(x: list[int]) -> list[int]:
    for i in range(0, len(x)):
        x[i] = x[i] *2
    # Don't forget to return your new list!
    return x


double_list(n))
print(double_list(n))
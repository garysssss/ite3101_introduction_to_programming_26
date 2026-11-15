from typing import List


def list_function(x: List[int]) -> int:
    return x[4]


n = [1,2,4,3, 5, 7]
print(list_function(n))

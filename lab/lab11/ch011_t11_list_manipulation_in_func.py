from typing import List
n = [3, 5, 7]

def list_extender(lst: List[int]) -> List[int]:
    lst.append(9)
    return lst

print(list_extender(n))

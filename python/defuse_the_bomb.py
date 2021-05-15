from typing import List
from icecream import ic


def decrypt(code: List[int], k: int) -> List[int]:
    """Naive approach: find the sum of the next k elements for each element

    If k < 0, reverse array then find the sum of next (-1)(k) elements"""
    n = len(code)
    res = []
    flag = False
    if k < 0:
        k *= -1
        code.reverse()
        flag = True

    for i in range(n):
        count = 0
        next = i + 1
        temp = 0
        while count < k:
            temp += code[next % n]
            count += 1
            next += 1

        res.append(temp)

    if flag:
        res.reverse()
    return res


if __name__ == "__main__":
    assert [0, 0, 0, 0] == ic(decrypt([1, 2, 3, 4], 0))
    assert [12, 10, 16, 13] == ic(decrypt([5, 7, 1, 4], 3))
    assert [12, 5, 6, 13] == ic(decrypt([2, 4, 9, 3], -2))

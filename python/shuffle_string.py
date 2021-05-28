from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    res = [None] * len(indices)
    for i, c in enumerate(s):
        res[indices[i]] = c
    res = "".join(res)
    return res


assert restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"

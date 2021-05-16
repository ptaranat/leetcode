def firstUniqChar(s: str) -> int:
    res = {i: s.count(i) for i in set(s)}
    for idx, char in enumerate(s):
        if res[char] == 1:
            return idx
    if all(i >= 2 for i in res.values()):
        return -1


if __name__ == "__main__":
    test_cases = ["leetcode", "loveleetcode", "aabb"]
    expected = [0, 2, -1]
    for test, output in zip(test_cases, expected):
        assert firstUniqChar(test) == output

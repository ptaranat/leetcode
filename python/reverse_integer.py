def reverse(num: int) -> int:
    """Reverse 32-bit integer"""
    rev = int(str(abs(num))[::-1])
    i = -rev if num < 0 else rev
    if i < -(2 ** 31) or i > 2 ** 31 - 1:
        return 0
    return i


assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
assert reverse(0) == 0
print("done")

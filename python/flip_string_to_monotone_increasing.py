def minFlipsMonoIncr(s: str) -> int:
    ones = flips = 0
    for bit in s:
        if bit == "0":
            if ones == 0:
                continue
            flips += 1
        else:
            ones += 1
        if ones < flips:
            flips = ones
    return flips


if __name__ == "__main__":
    test_cases = ["00110", "010110", "00011000"]
    expected = [1, 2, 2]
    for input, want in zip(test_cases, expected):
        got = minFlipsMonoIncr(input)
        assert got == want
        print(f"input: {input}\tgot {got} want {want}")

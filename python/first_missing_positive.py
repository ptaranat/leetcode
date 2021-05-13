from typing import List

# Hashing apporach, O(N) but O(N) extra space for hash set
def first_missing_positive(nums: List[int]) -> int:
    smallest = 1
    # Create a sets from array elements
    unique = {*nums}
    while True:
        if smallest not in unique:
            return smallest
        smallest += 1


if __name__ == "__main__":
    print(first_missing_positive([-1, 1, 2, 4, 5]))

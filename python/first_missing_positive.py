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


# Better version using O(1) extra space
# but it mutates the original list
def first_missing_positive_better(nums: List[int]) -> int:
    """Create an array the same length as the list,
    then put the elements where they belong.
    E.g [1, 2, 4, 5] goes into:
    index  :  1  2  3  4
    element: [1][2][4][5]

    If an element is not in the i-1 position (since indices start with 0)
    then there is a missing number we skipped over
    """
    n = len(nums)
    for i in range(n):
        while nums[i] - 1 in range(n) and nums[i] != nums[nums[i] - 1]:
            # Swap elements
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Instead of
    # return ([i == nums[i]-1 for i in range(n)] + [0]).index(False) + 1
    # use an iterator, otherwise we would use O(n) memory
    return next((i + 1 for i, num in enumerate(nums) if num != i + 1), n + 1)


if __name__ == "__main__":
    print(first_missing_positive([-1, 1, 2, 4, 5]))
    print(first_missing_positive_better([-1, 1, 2, 4, 5]))

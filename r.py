from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty, return 0
        if not nums:
            return 0
        # res keeps track of the position to insert the next unique element
        res = 1
        for i in range(1, len(nums)):
            # If current element is not equal to the previous, it's unique
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        # Return the number of unique elements
        return res

if __name__ == "__main__":
    # Sample test cases
    test_cases = [
        [1, 1, 2],
        [0,0,1,1,1,2,2,3,3,4],
        [],
        [1],
        [1,2,3,4,5]
    ]
    sol = Solution()
    for nums in test_cases:
        nums_copy = nums.copy()  # Copy to preserve original for printing
        k = sol.removeDuplicates(nums_copy)
        print(f"Input: {nums}")
        print(f"Output k: {k}, nums after removing duplicates: {nums_copy[:k]}")
        print("-" * 40)


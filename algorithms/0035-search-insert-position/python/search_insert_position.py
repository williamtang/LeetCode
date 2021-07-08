class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insert_idx = 0

        for idx, val in enumerate(nums):
            if val == target:
                return idx
            elif val > target:
                return insert_idx
            else:
                insert_idx = idx + 1

        return insert_idx


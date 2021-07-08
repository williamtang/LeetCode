class Solution:
    def search(self, nums, target):
        length = len(nums)
        left = 0
        right = length - 1

        while left <= right:
            # mid = left + (right-left)//2
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

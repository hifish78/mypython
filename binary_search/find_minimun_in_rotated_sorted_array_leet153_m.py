class Solution:
    """
    also compare with search_in_rotated_sorted_array in leetcode 33
    """
    def findMin(self, nums):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        if nums[left] > nums[right]:
            return nums[left]
        return nums[right]
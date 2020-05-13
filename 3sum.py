from typing import List


class Solution:
    def threeSum(self, nums):
        res = []
        if not nums or len(nums) < 3:
            return res
        nums.sort()
        for i in range(0, len(nums) - 2):
            # 枚举的那个数不能重复，去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # fix nums[i], then we should find the another 2 nums from i + 1 to len(nums) -1
            self.two_sums(nums, -nums[i], i + 1, len(nums) - 1, res)
        return res

    def two_sums(self, nums, target, left, right, res):
        while left < right:
            if nums[left] + nums[right] == target:
                item = []
                item.append(-target)
                item.append(nums[left])
                item.append(nums[right])
                res.append(item)
                left += 1
                right -= 1
                # left 已经 +1 了， left-1是之前的数字，left是新的，新的需要和原来的比，去重
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # right 已经 -1 了， right+1是之前的数字，right是新的，新的需要和原来的比，去重
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

# another solution
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = list()
        if not nums or len(nums) < 3:
            return res
        nums.sort()

        # fix one number (from the smallest to the largest)
        for i in range(0, len(nums) - 2):
            # 枚举的那个数不能重复，去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # fix nums[i], then we should find the another 2 nums from i + 1 to len(nums) -1
            left, right = i + 1, len(nums) - 1
            self.two_sums(nums, -nums[i], left, right, res)
        return res

    def two_sums2(self, nums, target, left, right, res):
        while left < right:
            while left < right and nums[left] + nums[right] < target:
                left += 1
            if left != right and nums[left] + nums[right] == target:
                item = []
                item.append(-target)
                item.append(nums[left])
                item.append(nums[right])
                res.append(list(item))
                # 去重 , (-1, 0, 1) 最后两个数去重， two-sum里面的去重
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            right -= 1
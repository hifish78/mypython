class Solution:
    def searchRange(self, nums, target):
        """
        time complexity: O(logN)
        space complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return [-1, -1]
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        res = [first, last]
        return res

    def find_first(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def find_last(self, nums, target):
        start, end = 0, len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

    def searchRange2(self, nums, target):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return [-1, -1]
        left_index , right_index = -1, -1

        for i in range(len(nums)):
            if nums[i] == target:
                left_index = i
                break
        if left_index == -1:
            return [-1, -1]

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_index = j
                break
        return [left_index, right_index]

sol = Solution()
nums = [1]
target = 1
res = sol.searchRange2(nums,target)
print(res)


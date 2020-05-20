class Solution:
    """
    二分搜索时每次都是把数组分成两部分，先判段哪一部分是有序的
    如果target在有序的那一部分，那么继续二分
    如果在无序的那一部分，重复第一步
    """

    # 一次二分法
    # 空间复杂度：O(N)
    # 时间复杂度：O(logN)
    def search(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            # 此时START 和MID都处在同一个递增数组上， 直接用原始的二分查找
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # 此时mid处于第二个递增数组 left处于第一个递增数组 自然的mid和right肯定处于第二个递增数组上
                # 还是直接运用原始的二分查找思想
                if target > nums[mid] and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    # nums[len(nums)-1] as 基准元素
    def search2(self, nums, target):
        # not nums <=> nums is None or len(nums) == 0
        if not nums:
            return -1

        # 找到拐点 minPos, 即第二个数组的起始位置
        left, right, minPos = 0, len(nums) - 1, 0
        while left + 1  < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        if nums[left] < nums[right]:
            minPos = left
        else:
            minPos = right

        # 判断target在哪一个数组中
        if target > nums[len(nums) - 1]:
            left = 0
            right = minPos - 1
        else:
            left = minPos
            right = len(nums) - 1

        # 对target所在数组二分搜索
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


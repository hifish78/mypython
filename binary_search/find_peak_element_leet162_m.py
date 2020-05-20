class Solution:
    """
    要点：
    由于题目中提示了要用对数级的时间复杂度，那么我们就要考虑使用类似于二分查找法来缩短时间，
    由于只是需要找到任意一个峰值，那么我们在确定二分查找折半后中间那个元素后，和紧跟的那个元素比较下大小，
    如果大于，则说明峰值在前面，如果小于则在后面。这样就可以找到一个峰值了
    """

    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return end
        else:
            return start
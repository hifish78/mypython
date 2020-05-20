class Solution:
    """
    滑动窗口问题
    [a, b, c, d, e], k = 3
    先求出前K个元素之和，例如 a + b + c
    然后遍历数组，减去头部元素（nums[i-k]),加上尾部元素(nums[i])

    滑动窗口问题思路和模版：窗口长度是k,
    1） 前K个元素进窗
    2） 对剩下的从第K个元素进行循环检测
        满足条件的加入结果集，
        左边的元素出窗
        左边的指针+1
    """
    def winSum(self, nums, k):
        if not nums or k <= 0:
            return []
        sum_k = 0
        res = []
        for i in range(k):
            sum_k = sum_k + nums[i]
        res.append(sum_k)

        for i in range(k, len(nums)):
            # 出窗： - nums[i-k]
            # 入窗： + nums[i]
            val = sum_k - nums[i - k] + nums[i]
            sum_k = val
            res.append(val)
        return res
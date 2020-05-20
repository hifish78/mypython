class Solution:
    """
    要点：
    1） 因为有重复数字，排序！
    2） 去重：if i >= 1 and i > index and nums[i-1] == nums[i]:
        i > index , 如果有2， 2'， 如果第一个2没有选中，第二个2'应该是在 i > index 以后，应该CONTINUE掉
    3） 和 subset_lint17_m.py 比较
    4） 时间复杂度： 2 exp（n)
    """
    def subsetsWithDup(self, nums):
        if nums is None:
            return None
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, subset, res):
        res.append(list(subset))

        for i in range(index, len(nums)):
            if i >= 1 and i > index and nums[i-1] == nums[i]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, res)
            subset.pop()
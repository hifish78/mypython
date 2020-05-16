class Solution:
    def subsets(self, nums):
        results = []
        if nums is None:
            return nums

        nums.sort()
        self.dfs(nums, 0, [], results)
        return results

    # 1. 递归的定义：在 Nums 中找到所有以 subset 开头的的集合，并放到 results

    def dfs(self, nums, index, subset, results):
        # 2. 递归的拆解
        # deep copy
        results.append(list(subset))

        for i in range(index, len(nums)):
            # [1] -> [1, 2]
            subset.append(nums[i])
            # 寻找所有以[1,2]开头的集合，并扔到results
            self.dfs(nums, i + 1, subset, results)
            # [1, 2] -> [1] ,backtracking
            subset.pop()


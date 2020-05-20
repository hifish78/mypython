class Solution:
    """
    要点：
    1） 先排序，避免重复 (如果题目已经告诉你没有重复的数字，这个不是必要的步骤）
    2） DFS:
        a) 加入第一个满足条件的结果， 注意是deep copy
           results.append(list(subset))
        b) for i in range(index, len(nums))
           遍历每个数字，加入到subset里面，  # [1] -> [1, 2]
        C) 从下个数字开始寻找所有以[1,2]开头的集合，并扔到results
            self.dfs(nums, i + 1, subset, results)
    """
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

    def subsets2(self, nums):
        res = []
        nums.sort()
        self.dfs2(nums, 0, [], res)
        return res

    def dfs(self, nums, index, subset, res):
        if index == len(subset):
            res.append(list(subset))
            return

        # 选了 nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, res)
        # 不选nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset, res)




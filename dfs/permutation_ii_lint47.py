class Solution:
    """
    要点： 如何去除重复
     if i - 1 >= 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                continue
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return nums
        res = []
        nums.sort()
        visited = [False for i in range(len(nums))]
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, item, res):
        if len(item) == len(nums):
            res.append(list(item))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i - 1 >= 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                continue

            item.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, item, res)
            item.pop()
            visited[i] = False
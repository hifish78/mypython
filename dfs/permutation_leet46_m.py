class Solution:
    """
    排列
    1)排列的递归退出条件： nums.length()  == permutation.size();
    2)需要有一个数组boolean visited[] 标记数组是否被选择过
    3)如果需要去除重复元素， 需要 Arrays.sort(nums), 并且判断：
     if (i-1 >=0 && nums[i] = nums[i-1] && !visited[i-1]) continue;
    4)时间复杂度： O（n!)， O(S*n*n),S是最后答案中soltion的个数

    组合：
    1)组合的递归退出条件： nums.length()  == startIndex;
    2)如果需要去除重复元素， 需要 Arrays.sort(nums), 并且判断：
    if (i-1 >=0 && nums[i] = nums[i-1] && i > startIndex);
    3)时间复杂度： 2 exp（n)
    """

    def permute(self,  nums):
        if nums is None:
            return nums
        res = []
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
            item.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, item, res)
            item.pop()
            visited[i] = False

sol = Solution()
nums = [1, 2, 3]
sol.permute(nums)
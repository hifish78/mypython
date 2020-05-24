class NumArray:
    """
    sums[i]: nums[0] + nums[1] +...+ nums[i-1]
    sums[i] 表示从从0到第i-1,总共i个元素之和
    sums[i] = sums[i-1] + nums[i-1]
    sums[0] = 0
    """

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
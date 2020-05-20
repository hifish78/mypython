class Solution:
    """
    要点：
    1） 用一个dictionary存储P{prefix sum ：prefix sum 第一次出现的最后一个元素的下标
    2） [1, 1, 1, 0, 1, 0, 0] -> [1, 1, 1, -1, 1, -1, -1]
        i = 0:  prefix sum is 1, prefix sum 1 第一次出现的最后一个元素的下标是 0 {1:0}
        i = 1:  prefix sum is 1+1, prefix sum 2 第一次出现的最后一个元素的下标是 0 {1:0, 2:1},
        i = 2:  prefix sum is 1+1+1, prefix sum 2 第一次出现的最后一个元素的下标是 0 {1:0, 2:0, 3:2}
        i = 3:  prefix sum is 1+1+1+ (-1) = 2, prefix sum 2 第一次出现的最后一个元素的下标是 1 （Not 3！！！）， ans = i - 1 = 3-1 =2

    """
    def findMaxLength(self, nums):
        presum_dict = {}
        ans = 0
        cur_sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_sum += -1
            else:
                cur_sum += 1

            # 特殊情况，表示从第0个元素到第i个元素和是0，直接i+1
            if cur_sum == 0:
                ans = i + 1
            elif cur_sum in presum_dict:  # cur_sum已经出现过, i 减去这个presum第一次出现第位置
                ans = max(ans, i - presum_dict[cur_sum])
            else:
                presum_dict = i  # 如果没有出现过，记录第一次出现第位置
        return ans




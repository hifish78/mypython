class Solution:
    """
    要点：
    我们维护一个一维动态数组 dp，其中 dp[i] 表示钱数为i时的最小硬币的数目。
    注意由于数组是从0开始的，所以要多申请一位，数组大小为 amount+1，这样最终结果就可以保存在 dp[amount] 中了。

    初始化 dp[0] = 0，因为目标值若为0时，就不需要硬币了。
    其他值可以初始化是 amount+1，为啥呢？因为最小的硬币是1，所以 amount 最多需要 amount 个硬币，amount+1 也就相当于当前的最大值了。
    注意这里不能用整型最大值来初始化，因为在后面的状态转移方程有加1的操作，有可能会溢出，除非你先减个1，这样还不如直接用 amount+1 舒服呢。

    要找状态转移方程了。回归例子1，假设我取了一个值为5的硬币，那么由于目标值是 11，所以是不是假如我们知道 dp[6]，那么就知道了组成 11 的 dp 值了？
    所以更新 dp[i] 的方法就是遍历每个硬币，如果遍历到的硬币值小于i值（比如不能用值为5的硬币去更新 dp[3]）时，用 dp[i - coins[j]] + 1 来更新 dp[i]，
    所以状态转移方程为： dp[i] = min(dp[i], dp[i - coins[j]] + 1);
    其中 coins[j] 为第j个硬币，而 i - coins[j] 为钱数i减去其中一个硬币的值，剩余的钱数在 dp 数组中找到值，然后加1和当前 dp 数组中的值做比较，
    取较小的那个更新 dp 数组。
    """
    def coinChange(self, coins, amount):
        dp = [ amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]

class Solution:
    '''
    1) Time complexity:  O(N×M).
    2) Space complexity: O(N×M).
    '''

    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
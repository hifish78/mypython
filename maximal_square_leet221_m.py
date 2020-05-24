class Solution:
    """
    我们约定$dp[i][j] $ 代表以（i,j）为右下角最大正方形的边长。
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxlen = 0

        # initialized m * n
        dp = [[0] * n for _ in range(m)]

        # 考虑边界条件： 第一行和第一列
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maxlen = max(maxlen, dp[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            maxlen = max(maxlen, dp[0][j])

        # 递推
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    maxlen = max(maxlen, dp[i][j])
                # else:
                #     dp[i][j] = 0  # no needed since it was initialized as '0'
        return maxlen * maxlen

    # Solution2: a little bit change, combining edge cases into the for loop
    def maximalSquare2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        maxlen = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                maxlen = max(maxlen, dp[i][j])
        return maxlen * maxlen


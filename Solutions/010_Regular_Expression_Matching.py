class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + i][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][i + 1] |= dp[i + 1][j]
                    else:
                        dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]
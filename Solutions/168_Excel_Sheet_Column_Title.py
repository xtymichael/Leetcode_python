class Solution:
# @param {integer} n
# @return {string}
    def convertToTitle(self, n):
        result = ''
        if n == 1:
            return 'A'
        while n > 0:
            r = n % 26
            if r == 0:
                result = 'Z' + result
                n -= 1
            else:
                result =  chr(r + 64) + result
            n /= 26
        return result


########## Solution 2 ####################
# class Solution:
# # @param {integer} n
# # @return {string}
#     def convertToTitle(self, n):
#         result = ''
#         if n > 26:
#             result = self.convertToTitle((n - 1)/ 26)
#         result += chr(65 + (n - 1) % 26)
#         return result

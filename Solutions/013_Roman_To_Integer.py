class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        Roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        newNum = 0

        if len(s) == 0:
            return None
        
        for i in range(len(s)):
            for j in range(len(num)):
                if s.find(Roman[j]) == 0:
                    newNum += num[j]
                    s = s[len(Roman[j]):]
                    break

        return newNum


######BETTER SOLUTION##############
# class Solution:
# # @param {string} s
# # @return {integer}
# def romanToInt(self, s):
#     roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
#     z = 0
#     for i in range(0, len(s) - 1):
#         if roman[s[i]] < roman[s[i+1]]:
#             z -= roman[s[i]]
#         else:
#             z += roman[s[i]]
#     return z + roman[s[-1]]
class Solution(object):
    def letterCombinations(self, digits):
            map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
            if len(digits) == 0: return []
            return [a+b for a in self.letterCombinations(digits[:-1])
                        for b in self.letterCombinations(digits[-1] )] or list(map[digits])
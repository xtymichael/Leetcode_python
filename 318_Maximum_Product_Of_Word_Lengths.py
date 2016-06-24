class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_len = map(lambda x: len(x), words)
        max_product = 0
        for i in range(len(words)):
            for j in range(i,len(words)):
                #if not list(set(words[i]) & set(words[j])): # too much time complexity
                word_set = list(set(words[i]))
                for char in words[j]:
                    if char in word_set:
                        break
                else:
                    max_product = max(max_product, words_len[i] * words_len[j])

        return max_product

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        answer = [0,1]

        while len(answer) < num + 1:
            answer.extend(map(lambda x:x+1, answer))

        return answer[:num+1]
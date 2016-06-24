class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        result = []
        for num in nums:
        	if num not in d:
        		d[num] = 0
        	d[num] += 1

        top_values = sorted(d.values())[-k:]
        for num in nums:
        	if  d[num] in top_values and num not in result:
        		result.append(num)
        return result


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return list(zip(*collections.Counter(nums).most_common(k))[0
        #return [i[0] for i in collections.Counter(nums).most_common(k)]
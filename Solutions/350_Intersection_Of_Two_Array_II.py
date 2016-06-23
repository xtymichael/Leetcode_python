class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        result = []
        for num in c1:
        	if num in c2:
        		result += [num] * min(c1[num], c2[num])

        return result
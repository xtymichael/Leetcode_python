class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = dict()
        result = []

        for num in nums1:
        	if num not in d:
        		d[num] = num

        for element in nums2:
        	if element in d and element not in result:
        		result.append(element)

        return result


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
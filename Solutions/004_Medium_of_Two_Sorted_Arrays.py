class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
    	temp = []
    	i = j = 0
    	while i < len(nums1) or j < len(nums2):
    		if i >= len(nums1):
    			temp += nums2[j:]
    			break

    		if j >= len(nums2):
    			temp += nums1[i:]
    			break

    		if nums1[i] <= nums2[j]:
    			temp.append(nums1[i])
    			i += 1

    		else:
    			temp.append(nums2[j])
    			j += 1

    	if len(temp) % 2 == 1:
    		return temp[len(temp)/2]
    	else:
    		return (temp[len(temp)/2] + temp[len(temp)/2 - 1]) / 2.0





################# LOG(N) BINARY SEARCH ###################
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):


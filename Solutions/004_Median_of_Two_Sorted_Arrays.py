#############   Bad Solution #########################

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
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n/2 + 1)
        else:
            smaller = self.findKth(A, B, n / 2)
            bigger = self.findKth(A, B, n / 2 + 1)
            return (smaller + bigger) / 2.0

    def findKth(self, A, B, k):
        if not A:
            return B[k - 1]
        if not B:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None

        if not b or (a is not None and a < b):
            return self.findKth(A[k / 2:], B, k - k / 2)
        return self.findKth(A, B[k / 2:], k - k / 2)

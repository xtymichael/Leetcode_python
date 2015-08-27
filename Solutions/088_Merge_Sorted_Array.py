class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        p, q, i = m - 1, n - 1, m + n - 1
        while q >= 0:
            if p < 0 or nums2[q] >= nums1[p]
                i -= 1
                q -= 1
                nums1[i] = nums2[q]
            else:
                i -= 1
                p -= 1
                nums1[i] = num1[p]
            






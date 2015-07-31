class Solution:
# @param {integer[]} nums
# @param {integer} k
# @return {void} Do not return anything, modify nums in-place instead.
	def rotate(self, nums, k):
		if k == 1:
			self.swap(nums[0],nums[-1])
		elif k != 0:
			for i in range(len(nums) / k):
				for j in range(k):
					self.swap(nums[i*k +j], nums[-k + j])
	def swap(self, a, b):
		temp = a
		a = b
		b = temp
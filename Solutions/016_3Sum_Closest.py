class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None
        if len(nums) == 3:
            return sum(nums)

        nums = sorted(nums)
        dlist = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = total - target
                if total == target:
                    return total

                if not dlist:
                    dlist.append(diff)
                elif abs(dlist[0]) > abs(diff):
                    dlist[0] = diff
                if j == k - 1 and 
                j += 1
        return dlist[0] + target
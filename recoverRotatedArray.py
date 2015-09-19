class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return nums
        for i in range(1, len(nums) ):
            if nums[i - 1] > nums[i ]:
                # print i
                self.reverse(nums, 0, i-1)
                self.reverse(nums, i , len(nums)-1)
                self.reverse(nums, 0, len(nums) - 1)
                return nums
    def reverse(self,nums, start, end):
        i = start
        j = end
        while i  < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i = i + 1
            j = j - 1
            
        return nums
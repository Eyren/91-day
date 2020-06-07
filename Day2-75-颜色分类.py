class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums)-1

        while curr <= p2: 
            if nums[curr] == 0:     #当前位为0，与第一位置换
                  nums[p0], nums[curr] = nums[curr], nums[p0]
                  p0 += 1
                  curr += 1
            elif nums[curr] == 2:   #当前位为2，置换到最后
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
                #curr += 1     #为2的时候，当前位不加1
            else:                   #当前位为1，位置不动，直接继续下一次循环
                curr += 1
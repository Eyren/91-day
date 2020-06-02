class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):            
            if digits[i] != 9:  #如果最后！=9,直接加1
                digits[i] += 1
                return digits
            else:               #==9,最后一位置0，进入下一次循环
                digits[i] = 0
                if digits[0] == 0:
                    digits.insert(0, 1)   #在数组最前面加一个数字1,其他位不管
                    return digits
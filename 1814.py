class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            ret = 0
            while num > 0:
                ret = ret * 10 + num % 10
                num //= 10
            return ret
        
        dic = {}
        mod = 1000000007
        count = 0
        for i in range(len(nums)):
            value = nums[i]-rev(nums[i])
            
            if value in dic:
                
                count = count%mod + dic[value]
                dic[value] +=1
            else:
                dic[value] =1
        return count % mod

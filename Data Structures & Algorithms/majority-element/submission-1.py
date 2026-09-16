class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        ele = nums[0]
        for i in range(1,len(nums)):
            if cnt==0:
                ele = nums[i]
            if nums[i]==ele:
                cnt+=1
            else:
                cnt-=1
            if cnt<=0:
                ele = nums[i]
        return ele

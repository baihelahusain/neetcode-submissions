class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        ele = 0
        for num in nums:
            d[num] = d.get(num, 0)+1
        
        for k, v in d.items():
            if v==max(d.values()):
                ele = k
        return ele

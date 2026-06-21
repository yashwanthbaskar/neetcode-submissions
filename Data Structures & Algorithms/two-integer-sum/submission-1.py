class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        seen={}
        for idx,num in enumerate(nums):
            if target - num in seen:
                ans.append(idx)
                ans.append(seen[target-num])
            seen[num]=idx
            
        if ans:
            if ans[1] < ans[0]:
                return ans[::-1]
        return ans

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[0]*len(nums)
        result=[]
        value1,value2=1,1
        for i in range(len(nums)):
            value1*=nums[i]
            prefix.append(value1)
        for i in range(len(nums)-1,-1,-1):
            value2*=nums[i]
            postfix[i]=value2
        result.append(postfix[1])
        # result[-1]=prefix[-2]
        for i in range(1,len(nums)-1):
            value=prefix[i-1]*postfix[i+1]
            result.append(value)
        result.append(prefix[-2])
        return result
        
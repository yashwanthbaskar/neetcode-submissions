class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        for char in s:
            if char not in seen:
                seen[char]=1
            else:
                seen[char]+=1
        
        for char in t:
            if char not in seen:
                seen[char]=1
            else:
                seen[char]-=1
        
        for k,v in seen.items():
            if v != 0:
                return False
        return True

        
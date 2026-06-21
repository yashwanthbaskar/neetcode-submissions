class Solution:
    def word2number(self,word):
        result=0
        for letter in word:
            result+=ord(letter)
        return result
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        features=[]
        for word in strs:
            result=self.word2number(word)
            features.append(result)
        d={}
        for feature_idx in range(len(features)):
            if features[feature_idx] not in d:
                d[features[feature_idx]]=[feature_idx]
            else:
                d[features[feature_idx]].append(feature_idx)
        result=[]
        for i,k in d.items():
            words=[]
            for idx in k:
                words.append(strs[idx])
            result.append(words)
        return result
        
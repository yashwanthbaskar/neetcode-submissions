class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded_string=''
        self.word_len=list(map(lambda x:len(x),strs))
        for word in strs:
            for letter in word:
                self.encoded_string+=letter
            self.encoded_string+='#'
        return self.encoded_string



    def decode(self, s: str) -> List[str]:
        decode_string=''
        decoded_strings=[]
        idx=0
        cnt=0
        for char in range(len(self.encoded_string)):
            if idx < len(self.word_len) and cnt==self.word_len[idx]:
                decoded_strings.append(decode_string)
                decode_string=''
                idx+=1
                cnt=0
                if self.encoded_string[char]=='#':
                    continue
            decode_string+=self.encoded_string[char]
            cnt+=1
            char+=1
        return decoded_strings


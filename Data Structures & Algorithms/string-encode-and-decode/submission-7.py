class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded =""
        for word in strs:
           encoded+=f"{len(word)}#{word}"
        
        return encoded


    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []

        output =[]

        i = 0 

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1
            
            curr_str_len = int(s[i:j])
            
            curr_str =  s[ j+1 : j+1 + curr_str_len ]
            output.append(curr_str)
            i = j+1+ curr_str_len
        return output


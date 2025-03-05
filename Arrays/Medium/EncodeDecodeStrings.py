from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        combinedString = ""
        
        # combine strings, delimiting each with their length and a #
        for i in strs:
            length = str(len(i))
            combinedString += length + "#" + i
        return combinedString

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0

        while i < len(s):
            j = i
            # this while loop captures full integer using the # delimiter
            while s[j] != "#":
                j += 1
            # grab the full integer
            length = int(s[i:j])

            # set i to the start of the string
            i = j + 1
            # set j to the end of the string
            j = i + length
            # slice the encoded string to separate it
            lst.append(s[i:j])
            # set i to the beginning of the next string
            i = j
            
        return lst
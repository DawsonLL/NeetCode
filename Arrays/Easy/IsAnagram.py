from typing import List
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the length of each list is unequal, we automatically know they cannot be anagrams
                return False
        
        # In Python, two dictionaries are equal if they have the same keys and same values associated with each key
        sdict = {}
        tdict = {}

        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1 # add the letter to the dictionary and increment its count
            tdict[t[i]] = tdict.get(t[i], 0) + 1

        return sdict == tdict # return true if equal, false otherwise
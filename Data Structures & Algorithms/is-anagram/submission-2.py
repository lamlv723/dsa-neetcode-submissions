class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}
        for char in s:
            counter_s[char] = counter_s.get(char, 0) + 1

        counter_t = {}
        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1

        # check
        for key in counter_s.keys():
            if counter_s[key] != counter_t.get(key, 0):
                return False

        return True
        

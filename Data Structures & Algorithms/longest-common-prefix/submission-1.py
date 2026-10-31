class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        base_str = strs[0]
        for i in range(len(base_str)):
            for s in strs:
                if i == len(s) or base_str[i] != s[i]:
                    return common_prefix

            # add character to prefix
            common_prefix += base_str[i]
        return common_prefix
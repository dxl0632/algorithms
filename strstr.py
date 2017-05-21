# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# other solutions:
# https://github.com/kamyu104/LeetCode/blob/master/Python/implement-strstr.py


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # brute force, O(mn)
        # need to consider edge cases
        # needle and/or haystack empty
        # needle length > haystack
        # two very long string?
        if needle == "":
            return 0
        if haystack == "":
            return -1
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

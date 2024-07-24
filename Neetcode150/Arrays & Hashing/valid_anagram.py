class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_stack = {}
        t_stack = {}
        for i in range(len(s)):
            s_stack[s[i]] = s_stack.get(s[i], 0) + 1
            t_stack[t[i]] = t_stack.get(t[i], 0) + 1

        for ch in s:
            if s_stack[ch] != t_stack.get(ch, 0):
                return False
        return True
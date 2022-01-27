"""
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
The lexicographically maximum substring is "bab".

Example 2:

Input: s = "leetcode"
Output: "tcode"
 

Constraints:

1 <= s.length <= 4 * 105
s contains only lowercase English letters.
"""

def lastSubstring(s: str) -> str:
        c = max(set(s))
        res = ''
        for i,x in enumerate(s):
            if x == c:
                res = max(res, s[i:])
        return res

print(lastSubstring("leetcode"))

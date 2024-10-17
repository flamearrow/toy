class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversedS = s[::-1]
        l = len(s)
        for i in range(l):
            if s[:l-i] == reversedS[i:]:
                return reversedS[:i]+s
        return ""


if __name__ == '__main__':
    # print(Solution().shortestPalindrome("abdfbag"))
    s = "123"

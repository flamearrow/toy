# Given two strings s1 and s2, return true if s2 contains a
# permutation
#  of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        permutes = []

        def permute(left, cur):
            if not left:
                permutes.append(cur)
            else:
                for i in range(len(left)):
                    permute(left[:i]+left[i+1:], cur+left[i])
        permute(s1, "")

        print(permutes)

        # for p in permutes:
        #     if p in s2:
        #         return True

        return False


if __name__ == '__main__':
    print(Solution().checkInclusion("abc", "eidbaooo"))
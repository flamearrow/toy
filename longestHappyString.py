# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case


import heapq

# greedy approcah - each time get a string from the one left most, that doesn't break the rule
# check the preivous two letters and avoid that letter if they are the same

# use a heap to keep track of left overs, always return the one with most value
# if the one with most value is excluded, pop the heap again and the the that value
# then push back if the nodes haven't reached to 0
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        left = [a, b, c]
        lMap = {0: 'a', 1: 'b', 2: 'c'}

        leftHeap = []
        if a > 0:
            heapq.heappush(leftHeap, [-a, 'a'])
        if b > 0:
            heapq.heappush(leftHeap, [-b, 'b'])
        if c > 0:
            heapq.heappush(leftHeap, [-c, 'c'])

        def letterWithMax(exceptLetter=None):
            # retIndex = -1
            # countMax = 0
            # for i in range(len(left)):
            #     if exceptLetter and lMap[i] == exceptLetter:
            #         continue
            #     else:
            #         if left[i] > countMax:
            #             countMax = left[i]
            #             retIndex = i

            # return retIndex

            if not leftHeap:
                return ""

            nextCount, nextChar = heapq.heappop(leftHeap)
            print(f"nextCount: {nextCount} nextChar: {nextChar}")
            if not exceptLetter:
                if -nextCount > 1:  # 0, don't push any more
                    heapq.heappush(leftHeap, [nextCount + 1, nextChar])
                return nextChar
            else:
                if nextChar == exceptLetter:  # need to get the next
                    if not leftHeap:
                        return ""
                    else:
                        retCount, retChar = heapq.heappop(leftHeap)
                        heapq.heappush(leftHeap, [nextCount, nextChar])
                        if -retCount > 1:
                            heapq.heappush(leftHeap, [retCount + 1, retChar])
                        return retChar
                else:
                    if -nextCount > 1:  # 0, don't push any more
                        heapq.heappush(leftHeap, [nextCount + 1, nextChar])
                    return nextChar

        ret = ""
        # nextLetterIndex = letterWithMax()
        # while nextLetterIndex != -1:
        #     nextLetter = lMap[nextLetterIndex]
        #     ret += nextLetter
        #     left[nextLetterIndex] -= 1

        #     if len(ret) >= 2 and ret[-2] == nextLetter: # avoid 3 in a row
        #         nextLetterIndex = letterWithMax(nextLetter)
        #     else:
        #         nextLetterIndex = letterWithMax()

        nextLetter = letterWithMax()
        while nextLetter:
            ret += nextLetter
            if len(ret) >= 2 and ret[-2] == nextLetter:
                print(f"excepting {nextLetter}")
                nextLetter = letterWithMax(nextLetter)
            else:
                nextLetter = letterWithMax()

        return ret

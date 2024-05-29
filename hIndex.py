from typing import List


class Solution:
    def __init__(self):
        pass

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # maxH = 0
        # for citation in citations:
        #     qualifiedPapersCount = len(list(filter(lambda x: x >= citation, citations)))
        #     maxH = max(maxH, min(qualifiedPapersCount, citation))
        # return maxH

        sortedCitations = sorted(citations)
        totalCount = len(sortedCitations)
        maxH = 0
        for index, citation in enumerate(sortedCitations):
            qualifiedPapersCount = totalCount - index
            maxH = max(maxH, min(qualifiedPapersCount, citation))
        return maxH



if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))

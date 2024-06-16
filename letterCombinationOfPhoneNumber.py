from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


class Solution:
    def __init__(self):
        self.lMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 1:
            print("here")
            return [c for c in self.lMap[digits[0]]]
        else:
            subCombinations = self.letterCombinations(digits[1:])
            ret = []
            for subCombination in subCombinations:
                for i in range(len(subCombination)):
                    newStr = subCombination[0:i] + digits[0] + subCombination[i:]
                    ret.append(newStr)
                ret.append(subCombination + digits[0])
            return ret


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
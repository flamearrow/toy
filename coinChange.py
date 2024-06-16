from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
import sys

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        else:
            coins.sort(reverse=True)
            ret = [-1]  # largest

            def search(index, amount, currentCoins):
                if amount == 0:
                    if ret[0] < 0:
                        ret[0] = currentCoins
                    else:
                        ret[0] = min(ret[0], currentCoins)
                else:
                    for i in range(index, len(coins)):
                        if coins[i] <= amount:
                            search(i, amount - coins[i], currentCoins + 1)

            search(0, amount, 0)

            return ret[0]

    def coinChangeDP(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1

        for value in range(amount + 1):
            for coin in coins:
                if value >= coin:
                    if dp[value - coin] != -1:
                        if dp[value] < 0:
                            dp[value] = dp[value - coin] + 1
                        else:
                            dp[value] = min(dp[value], dp[value - coin] + 1)
        return dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([3,7,405,436], 8839))
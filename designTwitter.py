# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
#
# Implement the Twitter class:
#
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId
#
# Example 1:
#
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
#
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

from typing import List


class Twitter:

    def __init__(self):
        # {follower: [followee]}
        self.follow_table = {}
        # tweets
        # (tweetId, userId), in order
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.insert(0, (tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        targetUsers = [userId]
        if userId in self.follow_table:
            targetUsers += self.follow_table[userId]
        for tweet in self.tweets:
            if tweet[1] in targetUsers:
                ret.append(tweet[0])
                if len(ret) == 10:
                    break
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_table:
            self.follow_table[followerId].append(followeeId)
        else:
            self.follow_table[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_table:
            self.follow_table[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:

if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 5)
    param_2 = obj.getNewsFeed(1)
    print(param_2)
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    param_3 = obj.getNewsFeed(1)
    print(param_3)
    # obj.unfollow(1, 2)
    # param_3 = obj.getNewsFeed(1)

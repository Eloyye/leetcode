import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.userTweets : dict[int, List[tuple[int, int]]] = defaultdict(list) # tuple (timestamp, tweetid)
        self.userFollowees : dict[int, set[int]] = defaultdict(set)
        self.global_time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.global_time, tweetId))
        self.global_time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.userFollowees[userId].add(userId)
        for followeeId in self.userFollowees[userId]:
            if followeeId in self.userTweets:
                index = len(self.userTweets[followeeId]) - 1
                timestamp, tweetId = self.userTweets[followeeId][index]
                heapq.heappush(minHeap, (timestamp, followeeId, tweetId, index - 1))

        while minHeap and len(res) < 10:
            timestamp, followeeId, tweetId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                #we can add the previous latest tweet from followeeID
                timestamp, new_tweet_id = self.userTweets[followeeId][index]
                heapq.heappush(minHeap, (timestamp, followeeId, new_tweet_id, index - 1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollowees and followeeId in self.userFollowees[followerId]:
            self.userFollowees[followerId].remove(followeeId)
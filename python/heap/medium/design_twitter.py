import heapq
import unittest
from collections import deque, defaultdict
from typing import List, Deque, Set, Tuple


class Twitter:

    def __init__(self):
        self.userPosts : dict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.userToFollowers: dict[int, Set[int]] = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.userToFollowers[userId]) if userId in self.userToFollowers else []
        users.append(userId)
        result, minHeap = [], []
        for user in users:
            if user in self.userPosts:
                minHeap.extend(self.userPosts[user])
        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            result.append( heapq.heappop(minHeap))
        return [timestamp_post[1] for timestamp_post in result]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.userToFollowers[followerId]:
            self.userToFollowers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.userToFollowers.get(followerId) and followeeId in self.userToFollowers[followerId]:
            self.userToFollowers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class TwitterTest(unittest.TestCase):
    def test1(self):
        twitter = Twitter()
        twitter.postTweet(1, 5)
        self.assertEqual(twitter.getNewsFeed(1), [5])
        twitter.follow(1,2)
        twitter.postTweet(2, 6)
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])
        twitter.unfollow(1, 2)
        self.assertEqual(twitter.getNewsFeed(1), [5])
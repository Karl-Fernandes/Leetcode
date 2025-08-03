class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([-self.timestamp, tweetId])
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.posts:
                index = len(self.posts[user]) - 1
                timestamp, tweetId = self.posts[user][index]
                heapq.heappush(minHeap, [timestamp, tweetId, user, index - 1])
        
        while minHeap and len(res) < 10:
            timestamp, tweetId, user, index  = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                timestamp, tweetId = self.posts[user][index]
                heapq.heappush(minHeap, [timestamp, tweetId, user, index - 1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
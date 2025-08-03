class Twitter:

    def __init__(self):
        self.posts = defaultdict(set)
        self.following = defaultdict(set)
        self.timestamp = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].add((-self.timestamp, tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId].copy()
        users.add(userId)
        
        # Use a heap to get most recent tweets efficiently
        heap = []

        for user in users:
            for timestamp, tweet in self.posts[user]:
                heapq.heappush(heap, (timestamp, tweet))
        
        # Get top 10 tweets by timestamp
        result = []
        for _ in range(min(10, len(heap))):
            result.append(heapq.heappop(heap)[1])
        
        return result
        

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
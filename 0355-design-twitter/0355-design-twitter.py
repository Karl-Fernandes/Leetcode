class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([tweetId, self.timestamp])

        if len(self.posts[userId]) > 10:
            self.posts[userId].pop(0)
        
        self.timestamp -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.following[userId].add(userId)
        
        for user in self.following[userId]:
            if user in self.posts:
                index = len(self.posts[user]) - 1
                tweetId, timestamp = self.posts[user][index]

                heapq.heappush(minHeap, [timestamp, tweetId, user, index - 1])
        
        while minHeap and len(res) < 10:
            timestamp, tweetId, user, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                tweetId, timestamp = self.posts[user][index]
                heapq.heappush(minHeap, [timestamp, tweetId, user, index - 1])
        
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        

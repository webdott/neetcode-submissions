class Twitter:
    def __init__(self):
        self.frc = defaultdict(set)
        self.posts = defaultdict(list)
        self.idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts[userId], [self.idx, userId, tweetId]);

        for followeeId in self.frc[userId]:
            heapq.heappush(self.posts[followeeId], [self.idx, userId, tweetId]);

        self.idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        return [c for a,b,c in heapq.nlargest(10, self.posts[userId])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId in self.frc[followeeId]:
            return None

        self.frc[followeeId].add(followerId)

        for t in self.posts[followeeId]:
            a, userId, c = t

            if userId == followeeId:
                heapq.heappush(self.posts[followerId], t);

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId not in self.frc[followeeId]:
            return None

        self.frc[followeeId].remove(followerId)

        i = 0
        while i < len(self.posts[followerId]):
            t = self.posts[followerId][i]
            a, userId, c = t

            if userId == followeeId:
                self.posts[followerId].pop(i)
                i -= 1

            i += 1   

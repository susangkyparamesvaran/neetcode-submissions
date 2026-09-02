class Twitter:

    def __init__(self):
        # keep track of who follows who
        self.followMap = {}
        # keeps track of the tweets of each user
        self.tweetMap = {}
        # the smaller the count the more recent the tweet
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count = self.count - 1

        if userId in self.tweetMap:
            (self.tweetMap[userId]).append((self.count, tweetId))
        else:
            self.tweetMap[userId] = [(self.count,tweetId)]


    def getNewsFeed(self, userId: int) -> List[int]:
        recent = []
        # list of tweets by the user or the people they follow
        feed = []
        # add own tweets
        for tweet in self.tweetMap.get(userId, []):
            feed.append(tweet)

        following = self.followMap.get(userId, [])

        for follow in following:
            if self.tweetMap[follow] == []:
                continue
            else:
                for tweet in self.tweetMap.get(follow,[]):
                    feed.append(tweet)
        
        heapq.heapify(feed)

        i = 0
        while (i < 10) and feed:
            count, tweet = heapq.heappop(feed)
            recent.append(tweet)
            i = i + 1
        
        return recent


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = []
        
        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].append(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

            if not self.followMap[followerId]:
                del self.followMap[followerId]
        

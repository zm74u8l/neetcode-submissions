class Twitter:

    def __init__(self):
        self.followers = {}
        self.time = 0
        self.posts = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = [] 
            
        self.posts[userId].append([self.time, tweetId])    
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        rlist = []
        if userId in self.posts:
            rlist.extend(self.posts[userId])

        if userId in self.followers:
            for user in self.followers[userId]:
                if user in self.posts:
                    rlist.extend(self.posts[user])

        rlist.sort(key=lambda x: x[0], reverse=True)

        return [item[1] for item in rlist[:10]]


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.followers:
            self.followers[followerId] = set()
        
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)

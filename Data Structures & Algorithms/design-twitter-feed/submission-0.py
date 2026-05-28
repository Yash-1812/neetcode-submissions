from typing import List
from collections import defaultdict

class Twitter:

    def __init__(self):
        # Maps userId to a list of tuples: (timestamp, tweetId)
        # Using a global timestamp counter ensures we know exactly which tweets are most recent.
        self.tweets = defaultdict(list)
        
        # Maps followerId to a SET of followeeIds so a user can follow multiple people.
        self.following_map = defaultdict(set)
        
        # Global tracker to order tweets from newest to oldest
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # We store the time with the tweet id so we can sort them later
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        
        # Start with the user's own tweets
        all_tweets = list(self.tweets[userId])
        
        # Add the tweets of everyone this user follows
        for followeeId in self.following_map[userId]:
            all_tweets.extend(self.tweets[followeeId])
            
        # Sort all gathered tweets by timestamp in descending order (newest first)
        all_tweets.sort(key=lambda x: x[0], reverse=True)
        
        # Extract just the top 10 tweetIds
        for i in range(min(10, len(all_tweets))):
            res.append(all_tweets[i][1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Users shouldn't follow themselves
        if followerId != followeeId:
            self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Safely remove the followee if they exist in the set
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
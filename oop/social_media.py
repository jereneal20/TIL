'''
Social Media Platform design. 
He asked me to give only 4 features. 
Post(Private and Public), Follow a user and Search.
It was HLD + LLD design. 
Asked me various approches by giving multiple scenarios of follower and followee. 
Went deep in Microservices architecture design.
OOD Code was expected.
'''
"""
* Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
"""
"""
- Like facebook
- Own feed -> list of docs (private/public)
 -> public: always be seen / private: only friend
 -> follow: doubly connected  (request & approve)
 -> doc search: keyword search globally (including friends private doc)

"""
# many user / many doc / generally not many, but someone has many follows
# post well (scaliability)
# efficiently get feed / efficiently get search result
# feed not real time

SocialMediaPlatform :
  DB_dict : user-id/doc
  -> post ( Doc , User)
  -> search (keyword)
	list of docs
  -> follow(User, User)
  -> unfollow(User, User)
  -> feed(User)
    list of docs
    

Doc (priv/pub):
   text
   user-id


User:
    UserID
    list<Document> documents # list of my Doc == Feed (ordered by time)
	set<User> friends
 

    follow(User)
    unfollow(User)
    post(Document)
    
Feed:
    
    


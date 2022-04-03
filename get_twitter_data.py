import tweepy

# 트위터 API 접근 위한 개인 키
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

# OAuth 핸들러 생성 & 개인정보 인증 요청
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 액세스 요청
auth.set_access_token(access_token, access_token_secret)
# api instace 생성
api = tweepy.API(auth)


# 기간별로 특정 키워드별 트윗을 따올 수 있다 하더라도 그렇게 세세하게 정보를 가공해서 점수화 할 수 있을까? 불가능하다고 생각
# 그래서 전체 트윗들의 팩터들을 누적해서 시간에 따른 변화량을 사용해보면 어떨까

# @akamirETH
def get_followers_TweetsInfos(id):
    followers = api.get_user(screen_name= id).followers_count
    tweets = api.user_timeline(screen_name = id, count=200) # 범위 : ~200

    print("followers: ",followers)
    print("------------------------")
    # 각 트윗별 likes & 총 트윗들의 likes
    likes = 0
    retweets = 0
    comments = 0 # This object is only available with the Premium and Enterprise tier products.
    for i in range(len(tweets)):
        print(i, "번 트윗")
        # comments += tweets[i].reply_count {Note: This object is only available with the Premium and Enterprise tier products.}
        likes += tweets[i].favorite_count
        retweets += tweets[i].retweet_count
        print("likes: ", tweets[i].favorite_count)
        print("retweets: ", tweets[i].retweet_count)
        print("-----------------------------------")

    print("total likes: ",likes)
    print("total retweets: ",retweets)
    print("-----------------------------------")

# main
get_followers_TweetsInfos("akamirETH")
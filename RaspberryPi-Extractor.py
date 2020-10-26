# Done using Twitter API search  hourly implementation.
import RPi.GPIO as GPIO
import datetime,requests
from google.cloud import firestore
from TwitterAPI import TwitterAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep

#Global variables
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, 0)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 0)
companies =['microsoft','tesla','spacex','cisco','apple','intel','netflix','qualcomm','marvell','comcast','starbucks','symantec','Nvidia','adobe','nasdaq','cree','Novavax','SteelDynamics','Geron','GileadSciences','ActivisionBlizzard','Fastenal']

 # Use the application default credentials
cred = credentials.Certificate('/home/DataExtractor-c129a8b176a8.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def collect_data(total_tweet):
    #twitter keys
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
    #twitter authentication
    api = TwitterAPI(consumer_key, 
                    consumer_secret,
                    access_key,
                    access_secret)


    #twitter search parameters
    for company in companies:
        search_text = company
        search ="#"+search_text
        tweet_count =100
        #search request
        public_tweets = api.request('search/tweets', {'q':search})

        for tweet in public_tweets:
                collection_name = 'final-data-'+search_text
                tweet_text =tweet['text']
                tweet_lang =tweet['lang']
                tweet_tags =tweet['entities']['hashtags']
                tweet_name = tweet['user']['screen_name']
                tweet_id =tweet['id']
                if  'possibly_sensitive' in tweet :
                    tweet_sensitive = tweet['possibly_sensitive']
                else :
                    tweet_sensitive = None
                tweet_retweet_count = tweet['retweet_count']
                tweet_if_retweeted =tweet['retweeted']
                tweet_favorite_count = tweet['favorite_count']
                tweet_if_favorite=tweet['favorited']
                tweet_timestamp = tweet['created_at']
                user_follower_count =tweet['user']['followers_count']
                verified_user =tweet['user']['verified']
                tweet_reply_id=tweet['in_reply_to_status_id']
                tweet_status =tweet['metadata']['result_type']
                
                
                if tweet_lang == "en" :
                    total_tweet+=1
                    print( str(total_tweet)+'===>>'+company)
                    data = {
                            u'Tweet Timestamp' : tweet_timestamp,
                            u'Tweet Entity tags': tweet_tags,
                            u'Favorite count' : tweet_favorite_count,
                            u'Favorited' : tweet_if_favorite,
                            u'Tweet Reply ID' : tweet_reply_id,
                            u'Tweet Sensitivity' : tweet_sensitive,
                            u'Retweet count' : tweet_retweet_count,
                            u'Retweeted' : tweet_if_retweeted,
                            u'Username' : tweet_name,
                            u'Tweet Status' : tweet_status,
                            u'User followers_count':user_follower_count,
                            u'Verified User' : verified_user,
                            u'Tweet text' : tweet_text
                    }

                    db.collection(collection_name).document(str(tweet_id)).set(data)
    print ("Executing sleep")

total_tweet =0
while True :
    url='http://www.google.com/'
    timeout=5
    try:
        some = requests.get(url, timeout=timeout)
        print("İnternet connection success.")
        val= True
    except requests.ConnectionError:
        print("İnternet connection failed.")
        val= False
    if val == True:
        try :
            GPIO.output(19,1)
            GPIO.output(26,1)
            collect_data(total_tweet)
            GPIO.output(26,0)
            GPIO.output(19,0)
            for x in range(0,1200):
                GPIO.output(19,1)
                sleep(1)
                GPIO.output(19, 0)
                sleep(1)
        except Exception as e :
            GPIO.output(19, 0)
            GPIO.output(26, 1)
            print("Internet connection broke in between transaction")
            print(e)
            sleep(300)
            GPIO.output(26, 0)
    else :
        GPIO.output(26, 1)
        sleep(300)
        GPIO.output(26, 0)

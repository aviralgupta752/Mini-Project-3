import twint
import nest_asyncio
nest_asyncio.apply()
import pandas as pd

def fetch_depressive_tweets(year):
	tags = ["#depression", "#anxiety", "#loneliness", "#hopelessness", "#depressed", '#antidepressants']
	for i in range(len(tags)):
		print(tags[i])
		c = twint.Config()
		# c.Format = "Tweet ID: {id} | Username: {username} | Tweet: {tweet}"
		c.Search = tags[i]
		c.Limit = 1000
		c.Year = year
		c.Store_csv = True
		c.Store_Object = True
		c.Output = "data/tweets_depressed.csv"
		c.Hide_output = True
		c.Stats = True
		c.Lowercase	= True
		c.Filter_retweets = True
		twint.run.Search(c)

def fetch_non_depressive_tweets(year):
	tags = ["#joy", "#happy", "#delight", "#cheer", "#bright", "#anger", "#fear"]
	for i in range(len(tags)):
		print(tags[i])
		c = twint.Config()
		# c.Format = "Tweet ID: {id} | Username: {username} | Tweet: {tweet}"
		c.Search = tags[i]
		c.Limit = 1000
		c.Year = year
		c.Store_csv = True
		c.Store_Object = True
		c.Output = "data/tweets_non_depressed.csv"
		c.Hide_output = True
		c.Stats = True
		c.Lowercase	= True
		c.Filter_retweets = True
		twint.run.Search(c)

years = [2020, 2021, 2022]

for year in years:
	fetch_depressive_tweets(year)
	fetch_non_depressive_tweets(year)


depressed_tweets = pd.read_csv("data/tweets_depressed.csv")
non_depressed_tweets = pd.read_csv("data/tweets_non_depressed.csv")

print("total depressed tweets: ", len(depressed_tweets))
print("total non-depressed tweets: ", len(non_depressed_tweets))






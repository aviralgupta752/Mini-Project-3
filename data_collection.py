import twint
import nest_asyncio
nest_asyncio.apply()
import pandas as pd


def fetch_data(data_type):
	tags = []
	file = ""

	if(data_type == "depressive"):
		tags = ["depression", "anxiety", "loneliness", "hopelessness", "depressed", 'antidepressants']
		file = "data/tweets_depressed.csv"

	else:
		tags = ["joy", "happy", "delight", "cheer", "bright", "anger", "fear"]
		file = "data/tweets_non_depressed.csv"


	start_dates = [f"2022-01-{day} 00:00:00" for day in range(10, 29)]
	end_dates = [f"2022-01-{day} 00:00:00" for day in range(11, 30)]

	for i in range(len(tags)):
		print(tags[i])

		for j in range(len(start_dates)):
			c = twint.Config()
			# c.Format = "Tweet ID: {id} | Username: {username} | Tweet: {tweet}"
			c.Limit = 1000

			c.Search = tags[i]
			c.Since = start_dates[j]
			c.Until = end_dates[j]
			c.Timedelta = 1
			c.Output = file

			c.Store_csv = True
			c.Store_Object = True
			c.Hide_output = True
			c.Stats = True
			c.Lowercase	= True
			c.Filter_retweets = True
			twint.run.Search(c)

fetch_data("depressive")
fetch_data("non-depressive")

depressed_tweets = pd.read_csv("data/tweets_depressed.csv")
non_depressed_tweets = pd.read_csv("data/tweets_non_depressed.csv")

print("total depressed tweets: ", len(depressed_tweets))
print("total non-depressed tweets: ", len(non_depressed_tweets))






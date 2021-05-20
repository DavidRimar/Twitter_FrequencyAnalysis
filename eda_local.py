from TweetCrawler import *
from config import *
import pandas as pd
from DataPreProcessor import *
from Model import Tweet, Place
from datetime_truncate import truncate

# INSTANTIATE TweetCrawler object
tweetCrawler = TweetCrawler(DATABASE_URI_TRIAL)

# SQL STATEMENTS
# statement = "SELECT twitter_id, text, places_full_name FROM test"
statement_temporal_day = "SELECT COUNT(date_trunc('day', created_at)) AS count, date_trunc('day', created_at) AS day FROM tweets GROUP BY date_trunc('day', created_at)"
statement_temporal_hour = "SELECT COUNT(date_trunc('hour', created_at)) AS count, date_trunc('hour', created_at) AS hour FROM tweets GROUP BY date_trunc('hour', created_at)"


statement_textual_generic = "SELECT * FROM tweets_hasgeo_fullarch_neg"

query_filter = ""

#statement_textual_bristol = 'SELECT text FROM tweets_hasgeo_fullarch_neg'
# statement_textual_bristol_2 = 'SELECT * FROM tweets_hasgeo_fullarch_neg WHERE "{column}" ILIKE %{keyword}%'.format(column=column,
#                                                                                                                   keyword=bristol)


# QUERY DATA AND STORE RESULTS
"""
results_temporal_day = tweetCrawler.crawl_data_with_connection(
    statement_temporal_day)

results_temporal_hour = tweetCrawler.crawl_data_with_connection(
    statement_temporal_hour)
"""
# results_textual_generic = tweetCrawler.crawl_data_with_connection(
#    statement_textual_generic)


results_textual_generic = tweetCrawler.crawl_data_with_session(
    Tweet, '%bristol%')
# print(type(results_textual_generic.iloc[1]['created_at']))
# print(results_textual_generic['created_at'].head())

results_textual_generic['created_at'] = results_textual_generic['created_at'].dt.floor(
    'd')

# results_textual_generic['created_at'] = results_textual_generic['created_at'].apply(
#    lambda L: datetime(L.year, L.month, L.day))

# truncate(results_textual_generic['created_at'], 'day')

# print(type(results_textual_generic_day.iloc[1]['created_at']))
# print(results_textual_generic['created_at'].head())

# CONVERT TO DATAFRAME
"""
df_temporal_day = pd.DataFrame(results_temporal_day.fetchall())
df_temporal_day.columns = results_temporal_day.keys()

df_temporal_hour = pd.DataFrame(results_temporal_hour.fetchall())
df_temporal_hour.columns = results_temporal_hour.keys()
"""
"""
df_textual_generic = pd.DataFrame(results_textual_generic.fetchall())
df_textual_generic.columns = results_textual_generic.keys()
"""
# INSPECT
# print("DAY:\n", df_temporal_day.head())
# print("HOUR:\n", df_temporal_hour.head())

# print("TEXT:\n", len(results_textual_generic))

# DATA PREPROCESSOR
data_pre_processor = DataPreProcessor(results_textual_generic)

# data_pre_processor.inspect_dates()
# convert to array
# data_pre_processor.convert_to_array(df_textual_generic)

# do all pre-processing steps (includes 1 remove stop words...)
# data_pre_processor.cleanse_all_tweets()

# inspect cleansed tweets
# data_pre_processor.inspect()

# data_pre_processor.show_word_frequencies(20)

w_df_per_day = data_pre_processor.create_wordfreq_per_day()

print(w_df_per_day)

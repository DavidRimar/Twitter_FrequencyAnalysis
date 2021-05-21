from TweetCrawler import *
from config import *
import pandas as pd
from DataPreProcessor import *
from Model import Tweet, Place
from datetime_truncate import truncate
from DataAnimator import *
from matplotlib.animation import FuncAnimation, PillowWriter
import bar_chart_race as bcr

# INSTANTIATE TweetCrawler object
tweetCrawler = TweetCrawler(DATABASE_URI_TRIAL)

# GET tweets
results_textual_generic = tweetCrawler.crawl_data_with_session(
    Tweet, '%bristol%')

# INSPECT
# print(type(results_textual_generic.iloc[1]['created_at']))
# print(results_textual_generic['created_at'].head())

# CONVERT 'created_at' to daily
results_textual_generic['created_at'] = results_textual_generic['created_at'].dt.floor(
    'd')

# results_textual_generic['created_at'] = results_textual_generic['created_at'].apply(
#    lambda L: datetime(L.year, L.month, L.day))

# DATA PREPROCESSOR
data_pre_processor = DataPreProcessor(results_textual_generic)

# GET WORD FREQ DATAFRAME PER DAY
w_df_per_day = data_pre_processor.create_wordfreq_per_day()

print(w_df_per_day)

# GET WORD FREQ DATAFRAME READY FOR ANIMATION
data_animator = DataAnimator(w_df_per_day)

bc_df = data_animator.convert_to_bc_format(w_df_per_day, 'data/result3.csv')

print(bc_df)

# loc_df = pd.read_csv('data/result3.csv', parse_dates=True, index_col=0)

bcr.bar_chart_race(
    df=bc_df,
    filename='example3.gif',
    orientation='h',
    sort='desc',
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.8,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total words: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(8, 3),
    dpi=144,
    cmap='prism',
    title='Twitter Word Frequencies By Day For "Bristol" Tweets',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family': 'DejaVu Sans', 'color': '.2'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)


# JUNK
# data_pre_processor.inspect_dates()
# convert to array
# data_pre_processor.convert_to_array(df_textual_generic)

# do all pre-processing steps (includes 1 remove stop words...)
# data_pre_processor.cleanse_all_tweets()

# inspect cleansed tweets
# data_pre_processor.inspect()

# data_pre_processor.show_word_frequencies(20)

from TweetCrawler import *
from config import *
import pandas as pd
from DataPreProcessor import *
from model.ModelBristol import *
from datetime_truncate import truncate
from DataAnimator import *
from matplotlib.animation import FuncAnimation
import bar_chart_race_master.bar_chart_race as bcr


def main():

    # INSTANTIATE TweetCrawler object
    tweetCrawler = TweetCrawler(DATABASE_URI_RDS_TWEETS)

    # GET tweets
    results_textual_generic = tweetCrawler.crawl_data_with_session(
        BristolSEM, text_filters=None, tweet_score=True)

    # CONVERT 'created_at' to daily
    results_textual_generic['created_at'] = results_textual_generic['created_at'].dt.floor(
        'd')

    # DATA PREPROCESSOR
    data_pre_processor = DataPreProcessor(results_textual_generic)

    # GET WORD FREQ DATAFRAME PER DAY (for top N words)
    w_df_per_day = data_pre_processor.create_wordfreq_per_day(20)

    w_df_per_day.to_csv('wordfreq/processed_tweets_bristol_scores_45.csv')

    # GET WORD FREQ DATAFRAME READY FOR ANIMATION
    data_animator = DataAnimator(w_df_per_day)

    bc_df = data_animator.convert_to_bc_format(
        w_df_per_day, 'data/bristol_scores_45.csv')

    # CREATE BARCHART RACE
    bcr.bar_chart_race(
        df=bc_df,
        filename='videos/bristol_scores_45.mp4',
        orientation='h',
        sort='desc',
        n_bars=20,
        fixed_order=False,
        fixed_max=False,
        steps_per_period=13,
        period_length=1300,
        end_period_pause=500,
        interpolate_period=False,
        period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
        period_template='%B %d, %Y',
        period_summary_func=lambda v, r: {'x': .98, 'y': .2,
                                          's': f'Total words: {v.sum():,.0f}',
                                          'ha': 'right', 'size': 11},
        perpendicular_bar_func='median',
        colors='prism',
        title='Twitter Word Frequencies By Day For Tweets with score 4 and 5',
        bar_size=.85,
        bar_textposition='inside',
        bar_texttemplate='{x:,.0f}',
        bar_label_font=7,
        tick_label_font=7,
        tick_template='{x:,.0f}',
        shared_fontdict=None,
        scale='linear',
        fig=None,
        writer=None,
        bar_kwargs={'alpha': .7},
        fig_kwargs={'figsize': (8, 3.5), 'dpi': 144},
        filter_column_colors=False)


if __name__ == "__main__":

    main()

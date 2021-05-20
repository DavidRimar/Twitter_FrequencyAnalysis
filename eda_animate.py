from TweetCrawler import *
from config import *
import pandas as pd
from DataPreProcessor import *
from Model import Tweet, Place
import datetime
import bar_chart_race as bcr
import matplotlib.pyplot as plt
from utils import *

# DUMMY DATA (after all preprocessing)
df = pd.read_csv('wordfreq.csv')

# print(df.head())

# replace "/" with "-"
df['time'] = df['time'].apply(lambda x: x.replace("/", "-", 2))

# convert string to Python datetime type
df['time'] = df['time'].apply(
    lambda x: datetime.datetime.strptime(x, '%d-%m-%Y'))

# print(df.head())

# CONVERT DF TO REQUIRED FORMAT


def convert_to_bc_format(dataframe):

    vocab = build_vocab(dataframe)

    dates = build_dates(dataframe)

    new_df = pd.DataFrame(index=dates, columns=vocab)

    for date in dates:

        # original dataframe
        date_rows = dataframe.loc[dataframe['time'] == date]

        for token in vocab:

            rel_row = date_rows.loc[date_rows['token'] == token]

            count_value = rel_row.loc[:, 'count'].values

            value = 1

            if count_value.size != 0:

                value = count_value[0]

            # print(type(value))
            # set value
            new_df.set_value(date, token, value)

    return new_df


def build_vocab(dataframe):

    token_array = dataframe.loc[:, 'token'].values

    vocab = []

    for token in token_array:

        if token not in vocab:

            vocab.append(token)

    print('VOCAB:', vocab)

    return vocab


def build_dates(dataframe):

    dates_array = dataframe.loc[:, 'time'].values

    unique_dates = []

    # add each unique date to the first column
    for time in dates_array:

        if time not in unique_dates:

            unique_dates.append(pd.Timestamp(time))

    return unique_dates


# PLOT IT
new_df = convert_to_bc_format(df)

new_df.index.name = 'date'
# new_df = new_df.set_index('datetime')
print(new_df.head())

print(type(new_df.index))


# final_df = pd.to_numeric(new_df, errors='coerce')


# print(type(new_df.iloc[2]['google']))

# new_df.to_csv('result.csv')
"""
df_values, df_ranks = bcr.prepare_wide_data(new_df, steps_per_period=4,
                                            orientation='h', sort='desc')
"""

# print(type(new_df.iloc[2]['google']))

sdf = load_dataset('local')

print(sdf.head())
# print(type(sdf.index))

# print(type(sdf.iloc[2]['Belgium']))

# adf = pd.read_csv('result.csv')

# print(adf.head())
# sdf.to_csv('covid.csv')

# ANIMATE IT

bcr.bar_chart_race(
    df=new_df,
    filename='ex3.html',
    orientation='h',
    sort='desc',
    n_bars=5,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total deaths: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='COVID-19 Deaths by Country',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family': 'Helvetica', 'color': '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)

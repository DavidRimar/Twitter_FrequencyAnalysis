from TweetCrawler import *
from config import *
import pandas as pd
import numpy as np
from DataPreProcessor import *
import datetime
import bar_chart_race as bcr
import matplotlib.pyplot as plt


class DataAnimator():

    ### CONSTRUCTOR ###
    def __init__(self, dataframe):

        self.dataframe_original = dataframe

    def convert_to_bc_format(self, dataframe, filepath):

        vocab = self.build_vocab(dataframe)

        dates = self.build_dates(dataframe)

        new_df = pd.DataFrame(index=dates, columns=vocab)

        new_df.index.name = 'date'

        for date in dates:

            # original dataframe
            date_rows = dataframe.loc[dataframe['date'] == date]

            for token in vocab:

                rel_row = date_rows.loc[date_rows['token'] == token]

                count_value = rel_row.loc[:, 'count'].values

                value = np.float64(1.0)

                if count_value.size != 0:

                    value = np.float64(count_value[0])

                # print(type(value))
                # set value
                new_df.set_value(date, token, value)

        # sort VALUES BY DATE
        new_df = new_df.sort_values("date", ascending=True)

        # save to csv then read it in
        new_df.to_csv(filepath)

        final_df = pd.read_csv(
            filepath, parse_dates=True, index_col=0)

        return final_df

    def build_vocab(self, dataframe):

        token_array = dataframe.loc[:, 'token'].values

        vocab = []

        for token in token_array:

            if token not in vocab:

                vocab.append(token)

        print('VOCAB:', vocab)

        return vocab

    def build_dates(self, dataframe):

        dates_array = dataframe.loc[:, 'date'].values

        unique_dates = []

        # add each unique date to the first column
        for time in dates_array:

            if time not in unique_dates:

                unique_dates.append(pd.Timestamp(time))

        return unique_dates

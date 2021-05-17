# import statments
import numpy
import re
import unicodedata
from nltk.corpus import stopwords
import nltk
import collections
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import contractions
from numpy.compat import unicode
import html
import inflect


"""
sources: 
1. https://gist.github.com/MrEliptik/b3f16179aa2f530781ef8ca9a16499af

2. https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/

"""


class DataPreProcessor():

    ### CONSTRUCTOR ###
    def __init__(self, text_to_cleanse):

        # nltk.download()

        ### INSTANCE VARIABLES ###
        self.raw_tweet_text_array = self.convert_df_to_array(text_to_cleanse)

        # 1.
        self.url_free_tweet_text_array = []

        # 2.
        self.capitalised_tweet_text_array = []

        # 3.
        self.stopwords_free_tweet_text_array = []

        self.cleansed_tweet_text_array = []

    # converts the text column of the DataFrame to array
    def convert_df_to_array(self, dataframe):

        return dataframe.loc[:, 'text'].values

    def remove_urls(self, tweet_text):
        """Replace URLs found in a text string with nothing
        (i.e. it will remove the URL from the string).

        Parameters
        ----------
        txt : string
            A text string that you want to parse and remove urls.

        Returns
        -------
        The same txt string with url's removed.
        """

        # url_free_array = []

        # for tweet in tweets_array:

        # append the url-free version of the tweet to the url-free array
        # url_free_array.append()

        # r'https?:\/\/\S*'
        # "([^0-9A-Za-z \t])|(\w+:\/\/\S+)"

        return " ".join(re.sub(r"http\S+", "", tweet_text).split())

    def fix_contractions(self, tweet_text):

        return contractions.fix(tweet_text)

    def unescape_html_entities(self, text):
        """Converts HTML entities to unicode."""
        text = html.unescape(text)
        return text

    def remove_non_ascii_characters(self, tweet_tokens):

        new_tokens = []

        for token in tweet_tokens:

            new_token = unicodedata.normalize('NFKD', token).encode(
                'ascii', 'ignore').decode('utf-8', 'ignore')

            new_tokens.append(new_token)

        return new_tokens

    def convert_to_lowercase(self, tokenized_tweet):

        tokenized_tweet_lc = []

        for word in tokenized_tweet:

            tokenized_tweet_lc.append(word.lower())

        return tokenized_tweet_lc

    def remove_punctuation(self, tweet_tokens):

        new_tokens = []
        for token in tweet_tokens:
            new_token = re.sub(r'[^\w\s]', '', token)
            if new_token != '':
                new_tokens.append(new_token)
        return new_tokens

    def replace_numbers_with_words(self, tweet_tokens):

        p = inflect.engine()

        new_tokens = []
        for token in tweet_tokens:
            if token.isdigit():
                new_token = p.number_to_words(token)
                new_tokens.append(new_token)
            else:
                new_tokens.append(token)
        return new_tokens

    # words is an array

    def remove_stopwords(self, single_tweet_tokenized):

        new_single_tweet = []

        for word in single_tweet_tokenized:

            if word not in stopwords.words('english'):

                new_single_tweet.append(word)

        return new_single_tweet

    def cleanse_single_tweet(self, single_tweet):

        # REMOVE URL
        single_tweet = self.remove_urls(single_tweet)

        # REMOVE CONTRACTIONs
        single_tweet = self.fix_contractions(single_tweet)

        # UNESCAPE HTML ENTITIES
        single_tweet = self.unescape_html_entities(single_tweet)

        # TOKENIZE WORDS
        tokenized_tweet = nltk.word_tokenize(single_tweet)

        # REMOVE NON-ASCII
        clean_tokenized_tweet = self.remove_non_ascii_characters(
            tokenized_tweet)

        # CONVERT TO LOWERCASE
        clean_tokenized_tweet = self.convert_to_lowercase(
            clean_tokenized_tweet)

        # REMOVE PUNCTUATION
        clean_tokenized_tweet = self.remove_punctuation(clean_tokenized_tweet)

        # REPLACE NUMBERS
        clean_tokenized_tweet = self.replace_numbers_with_words(
            clean_tokenized_tweet)

        # REMOVE STOP WORDS
        clean_tokenized_tweet = self.remove_stopwords(clean_tokenized_tweet)

        return clean_tokenized_tweet

    def cleanse_all_tweets(self):

        cleansed_tweets_array = []

        for tweet in self.raw_tweet_text_array:

            # cleansed version of the tweet
            cleansed_single_tweet = self.cleanse_single_tweet(tweet)

            # append to cleansed tweets array
            cleansed_tweets_array.append(cleansed_single_tweet)

        self.cleansed_tweet_text_array = cleansed_tweets_array

        return cleansed_tweets_array

    def inspect(self):

        print("RAW: ", self.raw_tweet_text_array[2])
        print("CLEANSED", self.cleansed_tweet_text_array[2])

        print("RAW: ", self.raw_tweet_text_array[3])
        print("CLEANSED", self.cleansed_tweet_text_array[3])

        """
        print("RAW: ", self.raw_tweet_text_array[2451])
        print("CLEANSED", self.cleansed_tweet_text_array[2451])
        """

    def flatten_words_from_tweets(self):

        flattened_word_corpus = [
            item for sublist in self.cleansed_tweet_text_array for item in sublist]

        return flattened_word_corpus

    def create_word_count_dict(self, number):

        words_dict = self.flatten_words_from_tweets()

        word_counts_dict = collections.Counter(words_dict)

        words_dict_top_n = pd.DataFrame(
            word_counts_dict.most_common(number), columns=['words', 'counts'])

        return words_dict_top_n

    def show_word_frequencies(self, number):

        # create a Pandas DataFrame with word counts
        words_dict_top_n = self.create_word_count_dict(number)

        fig, axis = plt.subplots(figsize=(8, 8))

        # Plot horizontal bar graph
        words_dict_top_n.sort_values(by='counts').plot.barh(x='words',
                                                            y='counts',
                                                            ax=axis,
                                                            color="blue")

        axis.set_title("Most Frequent Words Found in Tweets")

        plt.show()

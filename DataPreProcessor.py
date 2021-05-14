# import statments
import numpy
import re
from nltk.corpus import stopwords
import nltk


class DataPreProcessor():

    ### CONSTRUCTOR ###
    def __init__(self, text_to_cleanse):

        # nltk.download()

        ### INSTANCE VARIABLES ###
        self.raw_tweet_text_array = self.convert_text_to_array(text_to_cleanse)

        # 1.
        self.url_free_tweet_text_array = []

        # 2.
        self.capitalised_tweet_text_array = []

        # 3.
        self.stopwords_free_tweet_text_array = []

        self.cleansed_tweet_text_array = []

    # converts the text column of the DataFrame to array
    def convert_text_to_array(self, dataframe):

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

    def convert_to_lowercase(self, tokenized_tweet):

        tokenized_tweet_lc = []

        for word in tokenized_tweet:

            tokenized_tweet_lc.append(word.lower())

        return tokenized_tweet_lc

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

        # TOKENIZE WORDS
        tokenized_tweet = nltk.word_tokenize(single_tweet)

        # REMOVE NON-ASCII

        # CONVERT TO LOWERCASE
        clean_tokenized_tweet = self.convert_to_lowercase(tokenized_tweet)

        # REMOVE PUNCTUATION

        # REMOVE STOP WORDS
        cleans_tokenized_tweet = self.remove_stopwords(clean_tokenized_tweet)

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

        print("RAW: ", self.raw_tweet_text_array[14])
        print("CLEANSED", self.cleansed_tweet_text_array[14])

        print("RAW: ", self.raw_tweet_text_array[27])
        print("CLEANSED", self.cleansed_tweet_text_array[27])

        print("RAW: ", self.raw_tweet_text_array[3])
        print("CLEANSED", self.cleansed_tweet_text_array[3])

## **Word Frequency Analysis using Twitter**

This project uses a bank of tweets streamed from the Twitter API to build word frequency tables after a series of text pre-processing steps via the [DataPreProcessor](DataPreProcessor.py) class.

The word frequencies learned are then formatted to comform to the specific format that the bar_chart_race module can recognize via the [DataAnimator](DataAnimator.py) class.

The actual animation is implemented using [bar_chart_race](https://github.com/dexplo/bar_chart_race/).

Here are some example GIFs:

- Tweets containing references to "bristol"

![](videos/bristol_alltweets.gif)

- A small subset of 2733 Tweets that are definitely believed to be about the Bristol riots. The subset was obtained from the first
  dataset after assigning scores on the scale of 1 (very unlikely) and 5 (very likely) based on word co-occurrences such as "Bristol" and "riot".

![](videos/bristol_scores_45.gif)

from sqlalchemy.types import ARRAY, Float, JSON, Text, TEXT
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import ARRAY, Float
from geoalchemy2 import Geometry

Base = declarative_base()

"""
Tweet Class (extends Base class)
Representation of the data schema of the tables related to
the 'Bristol riots' event in the PostgreSQL.
"""


class BristolSEM(Base):
    __tablename__ = 'bristol_sem'
    id = Column(Integer, primary_key=True)  # Auto-generated ID
    tweet_id = Column(String)  # (data.id)
    text = Column(String)  # (data.text)
    created_at = Column(DateTime)  # (data.created_at)
    tweet_score = Column(Integer, nullable=True)

    # Constructor
    def __repr__(self):
        return "<Tweet(tweet_id='{}', text='{}', created_at={}, tweet_score={})>".format(self.tweet_id, self.text, self.created_at, self.tweet_score)

    def as_dict(self):

        tweet_as_dict = {'tweet_id': self.tweet_id,
                         'text': self.text,
                         'created_at': self.created_at,
                         'tweet_score': self.tweet_score}

        return tweet_as_dict


class BristolST(Base):
    __tablename__ = 'bristol_st'
    id = Column(Integer, primary_key=True)  # Auto-generated ID
    tweet_id = Column(String)  # (data.id)
    text = Column(String)  # (data.text)
    created_at = Column(DateTime)  # (data.created_at)
    final_point_lon = Column(DOUBLE_PRECISION)
    final_point_lat = Column(DOUBLE_PRECISION)
    final_point_astext = Column(Text)
    # STDBSCAN VARIATIONS (meter_minutes_minpts)
    # 3 DAY (4320 minutes)
    stdbscan_5000_4320_2 = Column(Integer, nullable=True)
    stdbscan_3500_4320_2 = Column(Integer, nullable=True)
    stdbscan_2500_4320_2 = Column(Integer, nullable=True)
    stdbscan_1000_4320_2 = Column(Integer, nullable=True)

    # 6 DAY (8640 minutes)
    stdbscan_5000_8640_2 = Column(Integer, nullable=True)
    stdbscan_3500_8640_2 = Column(Integer, nullable=True)
    stdbscan_2500_8640_2 = Column(Integer, nullable=True)
    stdbscan_1000_8640_2 = Column(Integer, nullable=True)

    # GEOMETRIC COLUMNS (bng)

    # Constructor
    def __repr__(self):
        return "<Tweet(tweet_id='{}', text='{}', created_at={}, final_point_lon={}, final_point_lat={}, final_point_astext={}, stdbscan_5000_4320_2={}, stdbscan_3500_4320_2={}, stdbscan_2500_4320_2={}, stdbscan_1000_4320_2={}, stdbscan_5000_8640_2={}, stdbscan_3500_8640_2={}, stdbscan_2500_8640_2={}, stdbscan_1000_8640_2={})>".format(self.tweet_id, self.text, self.created_at, self.final_point_lon, self.final_point_lat, self.final_point_astext, self.stdbscan_5000_4320_2, self.stdbscan_3500_4320_2, self.stdbscan_2500_4320_2, self.stdbscan_1000_4320_2, self.stdbscan_5000_8640_2, self.stdbscan_3500_8640_2, self.stdbscan_2500_8640_2, self.stdbscan_1000_8640_2)

    def as_dict(self):

        tweet_as_dict = {'tweet_id': self.tweet_id,
                         'text': self.text,
                         'created_at': self.created_at,
                         'final_point_lon': self.final_point_lon,
                         'final_point_lat': self.final_point_lat,
                         'final_point_astext': self.final_point_astext,
                         'stdbscan_5000_4320_2': self.stdbscan_5000_4320_2,
                         'stdbscan_3500_4320_2': self.stdbscan_3500_4320_2,
                         'stdbscan_5000_4320_2': self.stdbscan_2500_4320_2,
                         'stdbscan_1000_4320_2': self.stdbscan_1000_4320_2,
                         'stdbscan_5000_8640_2': self.stdbscan_5000_8640_2,
                         'stdbscan_3500_8640_2': self.stdbscan_3500_8640_2,
                         'stdbscan_2500_8640_2': self.stdbscan_2500_8640_2,
                         'stdbscan_1000_8640_2': self.stdbscan_1000_8640_2}

        return tweet_as_dict

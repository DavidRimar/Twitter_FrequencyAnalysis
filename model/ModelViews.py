from sqlalchemy.types import ARRAY, Float, JSON, DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import ARRAY, Float
from geoalchemy2 import Geometry

Base = declarative_base()

"""
BristolPlusView Class (extends Base class)
Representation of the data schema of bristol_plus_view materialized 
view in the PostgreSQL.
Keywords include: 
bristol protest riot march violence violent 
attack police officer bill scene fight disrupt siege
"""


class BristolPlusView(Base):
    __tablename__ = 'bristol_plus_view'
    id = Column(Integer, primary_key=True)  # Auto-generated ID
    tweet_id = Column(String)
    text = Column(String)
    created_at = Column(DateTime)
    geo_coordinates_coords = Column(ARRAY(DOUBLE_PRECISION), nullable=True)
    geo_place_id = Column(String, nullable=True)
    final_geom_point = Column(Geometry('POINT'), nullable=True)
    final_geom_point_astext = Column(String, nullable=True)
    final_geom_point_bgn = Column(Geometry('POINT'), nullable=True)

    # Constructor
    def __repr__(self):
        return "<Tweet(tweet_id='{}', text='{}', created_at={}, geo_coordinates_coords={}, geo_place_id={}, final_geom_points={}, final_geom_points_astext={}, final_geom_points_bgn={})>".format(self.tweet_id, self.text, self.created_at, self.geo_coordinates_coords, self.geo_place_id, self.final_geom_points, self.final_geom_points_astext, self.final_geom_points_bgn)

    def as_dict(self):

        tweet_as_dict = {'tweet_id': self.tweet_id,
                         'text': self.text,
                         'created_at': self.created_at,
                         'geo_coordinates_coords': self.geo_coordinates_coords,
                         'geo_place_id': self.geo_place_id,
                         'final_geom_points': self.final_geom_points,
                         'final_geom_points_astext': self.final_geom_points_astext,
                         'final_geom_points_bgn': self.final_geom_points_bgn}

        return tweet_as_dict

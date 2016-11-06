"""
Word count topology
"""

from streamparse import Grouping, Topology

from spouts.readHygiene import readHygiene
from bolts.yelpjoinbolt import YelpJoinBolt

class WordCount(Topology):
    yelp_spout = readHygiene.spec()
    yelp_bolt = YelpJoinBolt.spec(inputs={yelp_spout: Grouping.fields('hygiene_record')},
                             par=2)
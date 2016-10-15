"""
Word count topology
"""

from streamparse import Grouping, Topology

from bolts.yelpdatamain import YelpDataMainBolt
from spouts.yelp import YelpSpout


class WordCount(Topology):
    yelp_spout = YelpSpout.spec()
    new_count_bolt = YelpDataMainBolt.spec(inputs={yelp_spout: Grouping.fields('searchJson')},
                                        par=2)

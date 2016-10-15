"""
Word count topology
"""

from streamparse import Grouping, Topology

from bolts.wordcount import WordCountBolt
from spouts.yelp import YelpSpout


class WordCount(Topology):
    yelp_spout = YelpSpout.spec()
    new_count_bolt = WordCountBolt.spec(inputs={yelp_spout: Grouping.fields('searchJson')},
                                        par=2)

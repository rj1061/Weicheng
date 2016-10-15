"""
Word count topology
"""

from streamparse import Grouping, Topology

from bolts.wordcount import WordCountBolt
from spouts.words import WordSpout
from spouts.yelp import YelpSpout


class WordCount(Topology):
    word_spout = WordSpout.spec()
    yelp_spout = YelpSpout.spec()
    count_bolt = WordCountBolt.spec(inputs={word_spout: Grouping.fields('word')},
                                    par=2)
    new_count_bolt = WordCountBolt.spec(inputs={yelp_spout: Grouping.fields('something')},
                                        par=2)
"""
Word count topology
"""

from streamparse import Grouping, Topology

from spouts.readHygiene import readHygiene

class WordCount(Topology):
    yelp_spout = readHygiene.spec()

import unittest
import sys
import os

#we need to add the src folder to sys.path before being able to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils import Distance

class TestDistance(unittest.TestCase):

    def setUp(self):
        self.distance_km = Distance(5, "km")
        self.distance_m = Distance(100, "m")
        self.distance_miles = Distance(5, "miles")

    def test_distance_convert_1(self):
        self.distance_km.distance_convert("km", "m")
        self.assertAlmostEqual(self.distance_km.distance_value, 5000, "should be 5000")
        self.distance_m.distance_convert("m", "km")
        self.assertAlmostEqual(self.distance_m.distance_value, 0.1, "should be 0.1")
        self.distance_miles.distance_convert("miles", "km")
        self.assertAlmostEqual(self.distance_miles.distance_value, 8.047, "should be 8.047")
    
    #make a second function to again start with the distance_values initialised in the setUp method
    def test_distance_convert_2(self):
        self.distance_km.distance_convert("km", "miles")
        self.assertAlmostEqual(self.distance_km.distance_value, 3.107, "should be 3.107")
        self.distance_m.distance_convert("m", "miles")
        self.assertAlmostEqual(self.distance_m.distance_value, 0.062, "should be 0.062")
        self.distance_miles.distance_convert("miles", "m")
        self.assertAlmostEqual(self.distance_miles.distance_value, 8046.7, "should be 8046.7")
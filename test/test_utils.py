import unittest
import sys
import os

#we need to add the src folder to sys.path before being able to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from utils import Distance
from utils import Duration

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


class TestDuration(unittest.TestCase):

    def test_init(self):
        duration1 = Duration(1,30)
        self.assertAlmostEqual(duration1.minutes, 90, "Should be 90.")
        duration2 = Duration(2)
        self.assertAlmostEqual(duration2.minutes, 120, "Should be 120.")
        duration3 = Duration(minutes=150)
        self.assertAlmostEqual(duration3.minutes, 150, "Should be 150.")
        duration4 = Duration()
        self.assertAlmostEqual(duration4.minutes, 0, "Should be 0.")

    def test_short_str(self):
        duration1 = Duration(1,30)
        self.assertEqual(duration1.minutes, "1h30", "Should be 1h30.")
        duration2 = Duration(2)
        self.assertEqual(duration2.minutes, "2h0", "Should be 2h0.")
        duration3 = Duration(minutes=150)
        self.assertEqual(duration3.minutes, "2h30", "Should be 2h30.")
        duration4 = Duration()
        self.assertEqual(duration4.minutes, "0h0", "Should be 0h0.")

    def test_get_hours(self):
        duration1 = Duration(1,30)
        self.assertAlmostEqual(duration1.get_hours(), 1, "Should be 1.")
        duration2 = Duration(2)
        self.assertAlmostEqual(duration2.get_hours(), 2, "Should be 2.")
        duration3 = Duration(minutes=150)
        self.assertAlmostEqual(duration3.get_hours(), 2, "Should be 2.")
        duration4 = Duration()
        self.assertAlmostEqual(duration4.get_hours(), 0, "Should be 0.")

    def test_get_minutes(self):
        duration1 = Duration(1,30)
        self.assertAlmostEqual(duration1.get_minutes(), 30, "Should be 30.")
        duration2 = Duration(2)
        self.assertAlmostEqual(duration2.get_minutes(), 0, "Should be 0.")
        duration3 = Duration(minutes=150)
        self.assertAlmostEqual(duration3.get_minutes(), 30, "Should be 30.")
        duration4 = Duration()
        self.assertAlmostEqual(duration4.get_minutes(), 0, "Should be 0.")
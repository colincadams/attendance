from unittest import TestCase
import attendance

__author__ = 'colin'


class TestToId(TestCase):
    def test_to_id_1(self):
        text = "%2015000000048^STUDENT?;6278561000000534?"
        expected = "6278561000000534"
        actual = attendance.to_id(text)
        self.assertEqual(expected, actual)

    def test_to_id_2(self):
        text = "%2015000000048^STUDENT?;"
        expected = ""
        actual = attendance.to_id(text)
        self.assertEqual(expected, actual)

    def test_to_id_3(self):
        text = "6278561000000534"
        expected = "6278561000000534"
        actual = attendance.to_id(text)
        self.assertEqual(expected, actual)

    def test_to_id_3(self):
        text = ";6278561000000534?"
        expected = "6278561000000534"
        actual = attendance.to_id(text)
        self.assertEqual(expected, actual)
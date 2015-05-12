from unittest import TestCase
from attendance import Member

__author__ = 'colin'


class TestMember(TestCase):
    def test_here(self):
        member = Member("John", "Doe")
        self.assertFalse(member.attended)
        member.here()
        self.assertTrue(member.attended)
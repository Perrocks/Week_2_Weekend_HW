import unittest
from src.Song import *
from src.Guest import *
from src.Room import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("James Hetfield", 59, "Master of Puppets")
        self.guest_2 = Guest("Stevie Nicks", 74, "The Chain")
        self.guest_3 = Guest("Patrick Stump", 39, "Centuries")
        self.guest_4 = Guest("Johan Hegg", 49, "Twilight of the Thunder God")
        self.guest_5 = Guest("Trixie Mattel", 33, "Mama Don't Make Me Put on the Dress Again")


    def test_guest_has_name(self):
        self.assertEqual("James Hetfield", self.guest_1.guest_name)

    def test_guest_has_age(self):
        self.assertEqual(74, self.guest_2.age)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Centuries", self.guest_3.favourite_song)

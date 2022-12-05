import unittest
from src.Song import *
from src.Guest import *
from src.Room import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Master of Puppets", "Metallica", 515)
        self.song_2 = Song("The Chain", "Fleetwood Mac", 267)
        self.song_3 = Song("Centuries", "Fall Out Boy", 228)
        self.song_4 = Song("Twilight of the Thunder God", "Amon Amarth", 249)
        self.song_5 = Song("Mama Don't Make Me Put on the Dress Again", "Trixie Mattel", 179)
        self.song_6 = Song("Can I Play With Madness", "Iron Maiden", 212)
        self.song_7 = Song("Jolene", "Dolly Parton", 163)
        self.song_8 = Song("Paint It, Black","The Rolling Stones", 205)
        self.song_9 = Song("On the Road Again", "Willie Nelson", 154)
        self.song_10 = Song("Deutschland", "Rammstein", 323)

    def test_song_has_name(self):
        self.assertEqual("Master of Puppets", self.song_1.song_name)

    def test_song_has_artist(self):
        self.assertEqual("Fleetwood Mac", self.song_2.artist)

    def test_song_has_duration(self):
        self.assertEqual(228, self.song_3.song_duration)
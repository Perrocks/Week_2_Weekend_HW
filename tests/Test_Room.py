import unittest
from src.Song import Song
from src.Guest import Guest
from src.Room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Rock Room")
        self.room_2 = Room("Metal Room")
        self.room_3 = Room("Country Room")

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

        self.guest_1 = Guest("James Hetfield", 59, "Master of Puppets")
        self.guest_2 = Guest("Stevie Nicks", 74, "The Chain")
        self.guest_3 = Guest("Patrick Stump", 39, "Centuries")
        self.guest_4 = Guest("Johan Hegg", 49, "Twilight of the Thunder God")
        self.guest_5 = Guest("Trixie Mattel", 33, "Mama Don't Make Me Put on the Dress Again")


        
    def test_room_has_name(self):
        self.assertEqual("Rock Room", self.room_1.room_name)

    def test_room_is_empty(self):
        guests_in_room = len(self.room_2.guest_list)
        self.assertEqual(0, guests_in_room)
    
    def test_room_has_no_song(self):
        self.assertEqual([], self.room_3.current_song)

    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room_1.number_of_guests())

    def test_can_add_song_to_room(self):
        song = Song("Master of Puppets", "Metallica", 515)
        self.room_1.add_song(song)
        self.assertEqual(1, self.room_1.number_of_songs())


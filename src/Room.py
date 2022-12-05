class Room:
   def __init__(self, room_name):
        self.room_name = room_name
        self.current_song = []
        self.guest_list = []
   
   def number_of_guests(self):
        return len(self.guest_list)

   def number_of_songs(self):
        return len(self.current_song)
   
   def add_guest_to_room(self, guest):
      self.guest_list.append(guest)

   def add_song(self, song):
      self.current_song.append(song)



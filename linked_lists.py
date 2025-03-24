import song as sg

class SongNode:
    def __init__(self, song):
        self.song = song
        self.next = None

class PlayList:
    def __init__(self):
        self.head = None

    def add_song(self, name, artist, duration, route):
        new_song = sg.Song(name, artist, duration, route)
        if self.head is None:
            new_song.next = new_song
            self.head = new_song
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_song
            new_song.next = self.head        
     



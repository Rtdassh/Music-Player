import linked_lists as ll
import pygame
import customtkinter as ctk
import time

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        
        self.current_song = ""
        self.paused = True
        self.songs_list = []
        self.current_song_index = 0
        self.total_length = 0
        self.current_time = 0
        self.artist = "Unknown Artist"
        self.song_title = "No Song Selected"
        self.year = ""

        self.update_thread = None
        self.thread_running = False

    def browse_file(self):
        filetypes = (("MP3 Files", "*.mp3"), ("All files", "*.*"))
        filename = ctk.filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.add_song(filename)

    def add_song(self, filename):
        if filename not in self.songs_list:
            self.songs_list.append(filename)
            if len(self.songs_list) == 1:
                self.current_song_index = 0
                self.load_song()

    def load_song(self):
        if self.songs_list:
            self.current_song = self.songs_list[self.current_song_index]

    def play_pause(self):
        if not self.songs_list:
            self.browse_file()
            return
            
        if self.paused:
            try:
                if self.current_time == 0: 
                    pygame.mixer.music.load(self.current_song)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.play(start=self.current_time)               
                self.paused = False   

            except Exception as e:
                print(f"Error playing song: {e}")
        else:  
            pygame.mixer.music.pause()
            self.paused = True
    
    def stop(self):
        pygame.mixer.music.stop()
        self.paused = True
        self.current_time = 0

    def update_progress(self):
        while self.thread_running:
            if not self.paused and pygame.mixer.music.get_busy():
                self.current_time += 1
                
                if self.current_time >= self.total_length:
                    self.next_song()      
            time.sleep(1)

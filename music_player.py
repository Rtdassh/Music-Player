import linked_lists as ll
import pygame
import customtkinter as ctk
import os

track_name = ""
script_dir = os.path.dirname(os.path.abspath(__file__))
list_route = os.path.join(script_dir, "tracks")
track_route = os.path.join(list_route, track_name)
player = pygame.mixer.music

def main():
    pygame.init()
    player.load(track_route)
    player.play()
    window = ctk.CTk()
    window.title("Music Player")

    label_song = ctk.CTkLabel(window, text="Track Name")
    label_artist = ctk.CTkLabel(window, text="Artist")

    boton = ctk.CTkButton(window, text="Play", command = player.unpause, fg_color="red")
    botonStop = ctk.CTkButton(window, text="Pause", command=player.pause, fg_color="red")

    label_song.pack(pady=5)
    label_artist.pack(pady=5)
    boton.pack(pady=5)
    botonStop.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()

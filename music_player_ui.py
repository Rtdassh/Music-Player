import linked_lists as ll
import pygame
import customtkinter as ctk
import os
import music_player as mp


def main():
    player = mp.MusicPlayer()
    window = ctk.CTk()
    window.geometry("500x560")
    window.title("Music Player")

    label_song = ctk.CTkLabel(window, text="Track Name")
    label_artist = ctk.CTkLabel(window, text="Artist")

    boton = ctk.CTkButton(window, text="Play", command = player.play_pause, fg_color="#118AB2")
    botonStop = ctk.CTkButton(window, text="Add Song", command=player.browse_file, fg_color="red")

    label_song.pack(pady=5)
    label_artist.pack(pady=5)
    boton.pack(pady=5)
    botonStop.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()

import os

import pygame

import tkinter as tk
from tkinter import filedialog

from MusicPlayer import MusicPlayer

# Initialize Pygame
pygame.mixer.init()

# Initialize the music queue, current index, and folder path
music_queue = []
current_index = 0
folder_path = ""
paused = False

# Create an empty list for storing file names
file_names = []

# Declare listbox as a global variable
listbox = None

# Declare window as a global variable
window = None


def play():
    global music_queue, current_index, paused
    if not music_queue:
        return

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(music_queue[current_index])
        pygame.mixer.music.play()


def stop():
    global paused
    pygame.mixer.music.stop()
    paused = False


def pause():
    global paused
    pygame.mixer.music.pause()
    paused = True


def next_track():
    global current_index, paused
    if music_queue:
        current_index = (current_index + 1) % len(music_queue)
        play()
    else:
        paused = False


def previous_track():
    global current_index, paused
    if music_queue:
        current_index = (current_index - 1) % len(music_queue)
        play()
    else:
        paused = False


def select_folder():
    global folder_path, music_queue, file_names, listbox
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp3', '.wav', '.flac'))]
        selected_files = [os.path.join(folder_path, file) for file in selected_files]

        if selected_files:
            music_queue = selected_files
            file_names = [os.path.basename(file) for file in selected_files]

            if listbox:
                listbox.destroy()  # Destroy the old Listbox if it exists

            listbox = tk.Listbox(window, selectbackground = "#008CBA", font = ("Arial", 12))
            listbox.pack(fill = tk.BOTH, expand = True, padx = 20, pady = 10)

            for name in file_names:
                listbox.insert(tk.END, name)

            # print("Selected Files:", selected_files)  # Debugging output


def create_gui():
    global listbox, window  # Declare listbox and window as global variables

    window = tk.Tk()
    window.title("IgnoPlayer")

    # Customize the appearance with some styling
    window.geometry("1000x700")  # Set window size
    window.configure(bg="#f0f0f0")  # Set background color

    label = tk.Label(window, text="IgnoPlayer", bg="#f0f0f0", font=("Arial", 16))
    label.pack(pady=10)

    play_button = tk.Button(window, text = "▶ Play", command = play)
    stop_button = tk.Button(window, text = "⏹ Stop", command = stop)
    pause_button = tk.Button(window, text = "⏸ Pause", command = pause)
    next_button = tk.Button(window, text = "⏭ Next", command = next_track)
    prev_button = tk.Button(window, text = "⏮ Previous", command = previous_track)
    select_folder_button = tk.Button(window, text = "Select Folder", command = select_folder)

    play_button.pack(side = tk.LEFT, padx = 10)
    stop_button.pack(side = tk.LEFT, padx = 10)
    pause_button.pack(side = tk.LEFT, padx = 10)
    next_button.pack(side = tk.LEFT, padx = 10)
    prev_button.pack(side = tk.LEFT, padx = 10)
    select_folder_button.pack(side = tk.LEFT, padx = 10)

    listbox = tk.Listbox(window, selectbackground="#008CBA", font=("Arial", 12))
    listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_gui()

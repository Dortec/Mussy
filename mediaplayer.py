
# Import necessary libraries for audio handling, GUI elements, file operations, and randomization
import pygame.mixer
import tkinter as tk
import os
import random
from tkinter import PhotoImage, filedialog
from pygame.mixer_music import queue

# Initialize global variables for the media player
volume = 75  # Default volume level
currentSong = ""  # Variable to store the currently playing song
currentDirectory = "music/default_playlist/"  # Default directory for playlists
currentPlaylist = None  # List to store current playlist
maxIndex = 0  # Variable to store the index of the last song in the playlist
queue = {}  # Dictionary to map songs to their indices
index = 1  # Current index in the playlist

# Function Definitions

# Function to manage play and pause actions for the media player
def pauseplayState(window, timeSlider, playlistbox, pausePlaybutton, pauseIcon, playIcon):
    global currentSong  # Access the global variable to track the current song
    global maxIndex  # Access the global variable for the maximum index in the playlist
    global index  # Access the global index for the current position in the playlist

    # Print debugging information about the current state of the player
    print(index)
    print(maxIndex)
    print(currentSong)
    print(playlistbox.get(playlistbox.curselection()))

    # Check if the selected song in the playlist is different from the current song
    if not playlistbox.get(playlistbox.curselection()) == currentSong:
        print("Not the song, changing...\nNow playing: " + playlistbox.get(playlistbox.curselection()))
        # If different, start playing the selected song
        startSong(window, timeSlider, playlistbox, pausePlaybutton, pauseIcon)
    
    # If the same song is already playing, toggle play/pause based on current state
    elif pygame.mixer.music.get_busy():
        # If music is playing, pause it
        pygame.mixer.music.pause()
        # Update the button to reflect that music is paused (show play icon)
        pausePlaybutton.config(text="Pause", image=playIcon)
        # Update the window title to show the application name
        window.title("Mussy")
    else:
        # If music is paused, unpause it
        pygame.mixer.music.unpause()
        # Update the button to reflect that music is playing (show pause icon)
        pausePlaybutton.config(text="Play", image=pauseIcon)
        # Update the window title to show the current song name
        window.title(currentSong)
            
# Function to initiate song playback based on the current selection in the playlist
def startSong(window, timeSlider, playlistbox, pausePlaybutton, pauseIcon):
    global index  # Access the global variable that tracks the current index in the playlist
    global queue  # Access the global queue that maps song titles to their indices
    global currentSong  # Access the global variable that stores the currently playing song

    # Retrieve the selected song from the playlist box and set it as the current song
    currentSong = playlistbox.get(playlistbox.curselection())
    # Construct the full path to the song file
    song_path = currentDirectory + currentSong
    # Update the window title to reflect the currently playing song
    window.title(currentSong)
    # Configure the time slider to match the length of the song
    timeSlider.config(to=songLength())
    # Reset the time slider to the beginning
    timeSlider.set(0)
    # Load the song file into the music player
    pygame.mixer.music.load(song_path)
    # Start playing the song
    pygame.mixer.music.play()
    # Update the pause/play button to show the pause icon, indicating that music is playing
    pausePlaybutton.config(text="Play", image=pauseIcon)
    # Update the index of the current song in the global queue
    set_index()
    # Highlight the currently playing song in the playlist box
    playlistbox.selection_set(index)
    # Print the current index for debugging purposes
    print(index)
# Set the index of the current song in the queue
def set_index():
    global queue
    global currentSong
    global index
    index = queue[currentSong]

# Function to open a file dialog to select a new playlist directory
def openFile(playlistbox, window, timeSlider, pauseIcon, pausePlaybutton):
    global currentDirectory
    filepath = filedialog.askdirectory(initialdir="music/")
    currentDirectory = filepath
    songList(playlistbox)
# Function to stop music playback and reset the player state
def stop(timeSlider, pausePlaybutton, playIcon):
    pygame.mixer.music.pause()  # Pause the music
    pygame.mixer.music.set_pos(0)  # Reset the music position to the beginning
    timeSlider.set(0)  # Reset the time slider to zero
    pausePlaybutton.config(image=playIcon)  # Change the pause button to show the play icon

# Function to play the previous song in the playlist
def back(timeSlider, pausePlaybutton, pauseIcon, playlistbox):
    global index
    global queue
    global currentSong
    new_index = index - 2  # Calculate the index for the previous song
    next_song = playlistbox.get(new_index)  # Get the previous song from the playlist
    currentSong = next_song
    set_index()  # Update the index of the current song
    song_path = currentDirectory + next_song  # Create the full path for the song
    pygame.mixer.music.load(song_path)  # Load the song
    pygame.mixer.music.play()  # Play the song
    timeSlider.config(to=songLength())  # Update the time slider max value
    timeSlider.set(0)  # Reset the time slider to zero

# Function to skip to the next song in the playlist
def skip(timeSlider, pausePlaybutton, pauseIcon, playlistbox):
    global index
    global queue
    global currentSong
    next_song = playlistbox.get(index)  # Get the next song from the playlist
    song_path = currentDirectory + next_song  # Create the full path for the song
    currentSong = next_song
    set_index()  # Update the index of the current song
    song = pygame.mixer.Sound((currentDirectory + "/" + next_song))
    new_length = song.get_length()  # Get the length of the next song
    timeSlider.config(to=new_length)  # Update the time slider max value
    timeSlider.set(0)  # Reset the time slider to zero
    pygame.mixer.music.set_pos(songLength())  # Set the music position
    pygame.mixer.music.load(song_path)  # Load the song
    pygame.mixer.music.play()  # Play the song
    playlistbox.selection_set(index)  # Highlight the current song in the playlist

# Function to set the music volume based on slider value
def set_volume(slider_value):
    pygame.mixer.music.set_volume(float(slider_value))  # Set the music volume
    print("Volume: " + str(pygame.mixer.music.get_volume()))  # Print the current volume

# Function to set the music position based on time slider value
def set_time(slider_value):
    pygame.mixer.music.set_pos(float(slider_value))  # Set the music position

# Function to get the length of the current song
def songLength():
    song = pygame.mixer.Sound((currentDirectory + "/" + currentSong))
    return song.get_length()  # Return the length of the song

# Function to shuffle the current playlist
def shuffle(window, playlistbox, timeSlider, pauseIcon, pausePlaybutton):
    global currentPlaylist
    global index
    global queue
    global currentSong
    global maxIndex
    index = 0
    queue.clear()  # Clear the song queue
    currentPlaylist = search_mp3()  # Search for MP3 files in the current directory
    playlistbox.delete(0, tk.END)  # Clear the playlist box
    random.shuffle(currentPlaylist)  # Shuffle the list of MP3 files
    for file in currentPlaylist:  # Populate the playlist box with shuffled songs
        playlistbox.insert(tk.END, file)
        index += 1
        queue[file] = index
    maxIndex = index
    index = 0
    playlistbox.selection_set(index)  # Select the first song in the playlist
    currentSong = playlistbox.get(playlistbox.curselection())  # Set the current song
    song_path = currentDirectory + currentSong  # Create the full path for the song
    window.title(currentSong)  # Set the window title to the current song
    timeSlider.config(to=songLength())  # Update the time slider max value
    timeSlider.set(0)  # Reset the time slider to zero
    pygame.mixer.music.load(song_path)  # Load the song
    pygame.mixer.music.play()  # Play the song
    pausePlaybutton.config(text="Play", image=pauseIcon)  # Update the pause/play button
    set_index()  # Update the index of the current song

# Function to search the current directory for MP3 files
def search_mp3():
    mp3Files = [file for file in os.listdir(currentDirectory) if file.endswith(".mp3")]
    return mp3Files  # Return the list of MP3 files

# Function to display the list of songs in the playlist box
def songList(playlistbox):
    global currentPlaylist
    global queue
    global index
    global currentSong
    global maxIndex
    queue.clear()  # Clear the song queue
    currentPlaylist = search_mp3()  # Search for MP3 files in the current directory
    playlistbox.delete(0, tk.END)  # Clear the playlist box
    for file in currentPlaylist:  # Populate the playlist box with songs
        playlistbox.insert(tk.END, file)
        queue[file] = index
        index += 1
    maxIndex = index
    index = 0
    playlistbox.focus_set()  # Set focus on the playlist box
    playlistbox.selection_set(0)  # Select the first song in the playlist

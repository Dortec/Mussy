
# Import necessary libraries: Tkinter for GUI and pygame for audio handling
from tkinter import *
import pygame.mixer
from mediaplayer import *

# Initialize the mixer module from pygame for playing audio
pygame.mixer.init()

# Window settings
window = Tk()  # Create the main window object
window.geometry("183x200")  # Set the fixed size of the window
window.title("Mussy")  # Title of the window
window.resizable(False, False)  # Disable resizing of the window
fgColor = "#adbcc9"  # Foreground color used for text and highlights
bgColor = "#323347"  # Background color of the window
window.config(background=bgColor)  # Apply background color configuration

# Icons
# Load various icons for the GUI buttons from specified paths
pauseIcon = PhotoImage(file='icons/pause.png')
playIcon = PhotoImage(file='icons/play.png')
icon = PhotoImage(file='icons/icon.png')
refreshIcon = PhotoImage(file='icons/refresh.png')
shuffleIcon = PhotoImage(file='icons/dice.png')
folderIcon = PhotoImage(file='icons/folder.png')
fowardsIcon = PhotoImage(file='icons/fowards.png')
backwardsIcon = PhotoImage(file='icons/backwards.png')
optionsIcon = PhotoImage(file='icons/options.png')
stopIcon = PhotoImage(file='icons/stop.png')
window.iconphoto(True, icon)  # Set the icon for the window using the loaded icon image

# Widgets - Buttons
# Create buttons for various media player controls, set properties such as color, size, and commands
optionButton = Button(window,
   text="Options",
   command=lambda: pauseplayState(window, timeSlider, playlistbox, pausePlaybutton, pauseIcon, playIcon),
   highlightbackground=fgColor,
   bg=bgColor,
   fg=fgColor,
   activeforeground=fgColor,
   activebackground=bgColor,
   width=13,
   height=7,
   image=optionsIcon,
)
folderButton = Button(window,
    text="Folder",
    command=lambda: openFile(playlistbox, window, timeSlider, pauseIcon, pausePlaybutton),
    highlightbackground=fgColor,
    bg=bgColor,
    fg=fgColor,
    activeforeground=fgColor,
    activebackground=bgColor,
    image=folderIcon,
)
stopButton = Button(window,
   text="Stop",
   command=lambda: stop(timeSlider, pausePlaybutton, playIcon),
   highlightbackground=fgColor,
   bg=bgColor,
   fg=fgColor,
   activeforeground=fgColor,
   activebackground=bgColor,
   width=13,
   height=12,
   image=stopIcon,
)

backButton = Button(window,
   text="Backwards",
   command=lambda: back(timeSlider, pausePlaybutton, pauseIcon, playlistbox),
   highlightbackground=fgColor,
   bg=bgColor,
   fg=fgColor,
   activeforeground=fgColor,
   activebackground=bgColor,
   width=10,
   height=24,
   image=backwardsIcon,
)

fowardButton= Button(window,
   text="Fowards",
   command=lambda: skip(timeSlider, pausePlaybutton, pauseIcon, playlistbox),
   highlightbackground=fgColor,
   bg=bgColor,
   fg=fgColor,
   activeforeground=fgColor,
   activebackground=bgColor,
   width=10,
   height=24,
   image=fowardsIcon,
)

pausePlaybutton = Button(window,
   text="PausePlay",
   command=lambda: pauseplayState(window, timeSlider, playlistbox, pausePlaybutton, pauseIcon, playIcon),
   highlightbackground=fgColor,
   bg=bgColor,
   fg=fgColor,
   activeforeground=fgColor,
   activebackground=bgColor,
   image=playIcon,
)

shuffleButton = Button(window,
    text="Shuffle",
    command=lambda: shuffle(window, playlistbox, timeSlider, pauseIcon, pausePlaybutton),
    highlightbackground=fgColor,
    bg=bgColor,
    fg=fgColor,
    activeforeground=fgColor,
    activebackground=bgColor,
    image=shuffleIcon,
)
refreshButton = Button(window,
   text="Refresh",
   command=lambda: songList(playlistbox),
   highlightbackground=fgColor,
   bg=bgColor,
   fg=fgColor,
   activeforeground=fgColor,
   activebackground=bgColor,
   image=refreshIcon,
)

# Sliders
# Create sliders for volume and time, set properties such as orientation, colors, and command functions
volumeSlider = Scale(window,
   from_=1,
   to=0,
   resolution=0.01,
   bg=bgColor,
   foreground=fgColor,
   highlightbackground=fgColor,
   fg=fgColor,
   command=set_volume,
   orient='vertical',
   borderwidth=0,
   highlightthickness=0,
   relief='flat',
   troughcolor=fgColor,
   length=194,
   showvalue=False,
   width=11
)

timeSlider = Scale(window,
   from_=0,
   to=100,
   resolution=1,
   bg=bgColor,
   foreground=fgColor,
   highlightbackground=fgColor,
   fg=fgColor,
   command=set_time,
   orient='horizontal',
   borderwidth=0,
   highlightthickness=0,
   relief='flat',
   troughcolor=fgColor,
   width=16,
   length=162,
)

# Miscellaneous
playlistbox = Listbox(window,
  bg=bgColor,
  fg=fgColor,
  selectforeground=fgColor,
  selectbackground=bgColor,
  height=6,
  width=20,
)

# Widget placements
# Place all widgets in the window using absolute positioning
playlistbox.place(x=3, y=35)
pausePlaybutton.place(x=3, y=3)
refreshButton.place(x=137, y=3)
volumeSlider.place(x=169, y=3)
timeSlider.place(x=3, y=158)
folderButton.place(x=108, y=3)
shuffleButton.place(x=32, y=3)
backButton.place(x=61, y=3)
fowardButton.place(x=94, y=3)
stopButton.place(x=76, y=3)
optionButton.place(x=76, y=20)

# Initial settings
volumeSlider.set(0.75)  # Set the initial volume
playlistbox.focus_set()  # Focus on the playlist box
playlistbox.selection_set(0)  # Select the first item in the playlist
songList(playlistbox)  # Load songs into the playlist
window.mainloop()  # Start the main event loop of the GUI

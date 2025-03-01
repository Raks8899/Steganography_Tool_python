- Advanced Steganography Tool

  
This Python project implements a graphical Steganography Tool using Tkinter for the GUI and OpenCV/PIL for image processing. The application allows users to embed secret text messages inside image pixels and retrieve them later using a passcode.

📑 Code Structure and Explanation

1️⃣ Imports & Setup
python
Copy
Edit
import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import Label, Entry, Button, Text, Frame
from PIL import Image, ImageTk
cv2 (OpenCV): Handles image reading, manipulation, and saving.
tkinter: Used for creating the GUI (buttons, labels, file dialogs, etc.).
PIL (Pillow): Used to resize and display images inside the GUI.

2️⃣ Character Dictionaries
python
Copy
Edit
d, c = {}, {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
d maps characters to their ASCII values.
c maps ASCII values back to characters.
These mappings are used to embed and extract message characters in/from image pixels.

3️⃣ Global Variables
python
Copy
Edit
img, image_path = None, ""
max_message_length = 0
img: Holds the loaded image (as OpenCV matrix).
image_path: Stores the path to the loaded image.
max_message_length: Maximum number of characters that can be hidden in the selected image.

4️⃣ Image Loading Function
python
Copy
Edit
def load_image():
    ...
Opens a file dialog for the user to select an image.
Loads the image using OpenCV (cv2.imread()).
Displays the image inside the GUI using PIL & ImageTk.
Computes the maximum message length based on image size (each pixel can hold 3 characters).

5️⃣ Character Count Updater
python
Copy
Edit
def update_char_count(*args):
    ...
This updates the live character count while typing the secret message.
Ensures the message fits within the available capacity.

6️⃣ Encryption Function
python
Copy
Edit
def encrypt_message():
    ...
Hides each character into the pixel values (R, G, B).
Uses a loop over characters and assigns ASCII values into image pixels.
Saves the modified image via cv2.imwrite() after encoding.
Displays a progress bar during the process.

7️⃣ Decryption Function
python
Copy
Edit
def decrypt_message():
    ...
Reads pixel values and converts them back to characters using the ASCII mapping (c).
Assembles and displays the decrypted message.
Only decrypts if the correct passcode is provided.

8️⃣ Clear Function
python
Copy
Edit
def clear_all():
    ...
Clears all user inputs, logs, and resets the image display.
Helpful when switching to a new image.

9️⃣ Log Function
python
Copy
Edit
def log_message(msg, level="info"):
    ...
Appends color-coded logs to the log console.
Log levels: success, error, info, each with a different color.

🔟 Log Saving Function
python
Copy
Edit
def save_log():
    ...
Writes the log console contents to a text file (steganography_log.txt).
Provides a permanent record of activity.


1️⃣1️⃣ Theme Toggle Function
python
Copy
Edit
def toggle_theme():
    ...
Switches between a dark hacker-style theme and a light theme.
Updates background, text colors, and widget appearances dynamically.


1️⃣2️⃣ GUI Setup (Main Window)
python
Copy
Edit
root = tk.Tk()
root.title("Steganography Tool - Advanced")
...
Sets up the main window title, size, and background color.
Defines all labels, buttons, entries, text areas, and progress bar.
Buttons are linked to their respective functions (encrypt, decrypt, load image, etc.).

1️⃣3️⃣ Image Display Area
python
Copy
Edit
img_label = Label(root, ...)
...
This is a Label widget where the selected image is displayed after resizing.

1️⃣4️⃣ Message and Passcode Inputs
python
Copy
Edit
msg_entry = Entry(root, ...)
pass_entry = Entry(root, ...)
decrypt_pass_entry = Entry(root, ...)
Text entry widgets where users type:
Secret message to hide.
Passcode to protect the message.
Passcode to unlock the message.

1️⃣5️⃣ Log Console
python
Copy
Edit
log_console = Text(root, ...)
Text area where all logs (success/error/info) are shown to the user in real-time.

1️⃣6️⃣ Progress Bar
python
Copy
Edit
progress_bar = ttk.Progressbar(root, ...)
Displays progress animation during encryption/decryption to indicate processing.

1️⃣7️⃣ Main Loop
python
Copy
Edit
root.mainloop()
Starts the Tkinter event loop, keeping the window open and interactive.

🧩 Data Encoding Process Summary
Encoding (Encryption)
Each character's ASCII value is stored in a single color channel (R, G, B) of each pixel.
Example:
First pixel's red channel gets the first character.
First pixel's green channel gets the second character.
First pixel's blue channel gets the third character.
Continues pixel by pixel until the whole message is encoded.
Decoding (Decryption)
The reverse of the encoding process.
Reads characters back from each pixel’s R, G, B channels.
Combines all characters into the full message.
🕵️ Security Note
The passcode check is only applied before decryption, but it does not encrypt the image itself.
To make it more secure, you could consider adding encryption to the message itself before hiding it in the image.

✅ Key Functions Summary Table
Function	Purpose
load_image()	Load and display image
encrypt_message()	Hide message into image
decrypt_message()	Extract hidden message
clear_all()	Reset UI and clear data
log_message()	Add color-coded log message
save_log()	Save logs to file
toggle_theme()	Switch between dark/light modes
update_char_count()	Show live character count








    ...



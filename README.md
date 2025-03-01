 Advanced Steganography Tool
 

📌 Overview
This Python-based Steganography Tool allows users to hide secret messages inside images and later retrieve them using a passcode. The tool provides a graphical user interface (GUI) built with Tkinter and utilizes OpenCV/PIL for image processing.


📑 Code Structure & Explanation

1️⃣ Imports & Setup
The code imports essential libraries:

cv2 (OpenCV) - Image processing.
tkinter - GUI elements.
PIL (Pillow) - Image manipulation for display.

2️⃣ Character Dictionaries for Encoding
python
Copy
Edit
d, c = {}, {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
These dictionaries convert characters to ASCII values and back. They are used when hiding and extracting messages.


3️⃣ Image Handling Functions
📌 Load & Display Image
python
Copy
Edit
def load_image():
    ...
Opens a file dialog for selecting an image.
Loads the image using OpenCV.
Resizes it for display using PIL.
Calculates maximum message length based on image size.
📌 Update Character Count
python
Copy
Edit
def update_char_count(*args):
    ...
Updates the character count as the user types a message.

4️⃣ Message Encoding (Hiding Secret Text)
python
Copy
Edit
def encrypt_message():
    ...
Hides each ASCII character inside the pixel’s R, G, B values.
Saves the modified image with the embedded message.

5️⃣ Message Decoding (Extracting Hidden Text)
python
Copy
Edit
def decrypt_message():
    ...
Reads pixel values to reconstruct the original text.
Requires the correct decryption passcode.

6️⃣ GUI Components
The tool provides a modern hacker-style GUI with:

Dark Theme & Light Mode Toggle
Log Console for User Feedback
Progress Bar for Processing Animation
Clear Button to Reset Fields

7️⃣ Logging & Saving Activity
python
Copy
Edit
def log_message(msg, level="info"):
    ...
Displays success, error, and info messages with different colors.
📌 Save Log to File
python
Copy
Edit
def save_log():
    ...
Saves the log messages to steganography_log.txt.
🛠 Features
✔ Hide secret text inside images
✔ Retrieve hidden messages
✔ Password protection for decryption
✔ Modern GUI with theme toggle
✔ Logs & progress tracking


🔐 Security Note
Message security depends on password protection.
Consider encrypting the text itself before embedding.
📌 Key Functions Table
Function	Purpose
load_image()	Load and display image
encrypt_message()	Hide message inside image
decrypt_message()	Extract hidden message
clear_all()	Reset UI and clear data
log_message()	Add logs to UI console
save_log()	Save logs to file
toggle_theme()	Switch dark/light mode

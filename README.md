Advanced Steganography Tool







Introduction
This Advanced Steganography Tool allows you to hide secret messages inside images using pixel manipulation techniques. It also provides features for decrypting hidden messages, saving logs, and switching between light and dark themes for better user experience.

This project uses Python, OpenCV, and Tkinter for the graphical interface and steganography functionality.

📸 Features
📂 Load Image: Select an image file to encode your secret message into.
🔐 Encrypt Message: Hide a message inside the image using pixel encoding.
🔓 Decrypt Message: Retrieve the hidden message from the encoded image using the correct passcode.
💾 Save Logs: Save the log of activities and errors to a file for record keeping.
🎨 Dark/Light Mode: Toggle between hacker-style dark theme and clean light theme.
🧹 Clear All: Reset all inputs, logs, and images.
🛠️ Technologies Used
Python 3.8+
Tkinter (for GUI)
OpenCV (for image processing)
Pillow (PIL) (for image handling)
TTK Widgets (for progress bar)
📂 Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/Advanced-Steganography-Tool.git
cd Advanced-Steganography-Tool
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Requirements file content:

Copy
Edit
opencv-python
pillow
Run the tool:

bash
Copy
Edit
python steganography_tool.py
🖼️ Screenshot
Dark Mode	Light Mode
(You can update the above URLs with actual screenshots from your project.)

🔑 How It Works
Load Image - Choose any image (JPG, PNG, JPEG) to encode your message.
Enter Message - Type the secret message you want to hide.
Set Passcode - Enter a passcode required for decryption.
Encrypt & Save - The message gets encoded into the image, and you can save the result.
Decrypt - Using the correct passcode, the hidden message can be retrieved.
Logs - All actions and errors are logged to the log window and can be saved to steganography_log.txt.
📖 File Structure
bash
Copy
Edit
📂 Advanced-Steganography-Tool/
├── steganography_tool.py        # Main Python file (your provided code)
├── requirements.txt             # Required dependencies
├── README.md                     # Project Documentation (this file)
└── steganography_log.txt         # Log file (generated after running the tool)
🖥️ Usage Example
text
Copy
Edit
1. Launch the application.
2. Load an image.
3. Enter your secret message and passcode.
4. Click "Encrypt & Save" to create a stego-image.
5. Reload the saved image to decrypt using the same passcode.
6. View logs and save them if necessary.
⚠️ Note
Passcode is required for both encryption and decryption.
If the passcode is incorrect, decryption will fail.
Maximum message length depends on image size.

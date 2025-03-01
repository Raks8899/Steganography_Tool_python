import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import Label, Entry, Button, Text, Frame
from PIL import Image, ImageTk

# Character dictionary
d, c = {}, {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

img, image_path = None, ""
max_message_length = 0


def load_image():
    global img, image_path, max_message_length
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if image_path:
        img = cv2.imread(image_path)
        pil_image = Image.open(image_path).resize((200, 200), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(pil_image)
        img_label.config(image=tk_image)
        img_label.image = tk_image
        log_message(f"Loaded: {os.path.basename(image_path)}", "info")

        h, w, _ = img.shape
        max_message_length = (h * w * 3) // 8
        char_count_label.config(text=f"Max Length: {max_message_length} chars")


def update_char_count(*args):
    char_count_label.config(text=f"Chars: {len(msg_entry.get())}/{max_message_length}")


def encrypt_message():
    if img is None:
        log_message("No image loaded!", "error")
        return

    msg, password = msg_entry.get(), pass_entry.get()

    if not msg or not password:
        log_message("Message & password required.", "error")
        return

    if len(msg) > max_message_length:
        log_message(f"Message too long. Max: {max_message_length} chars.", "error")
        return

    n, m, z = 0, 0, 0
    progress_bar.start()
    for i, char in enumerate(msg):
        img[n, m, z] = d[char]
        n, m, z = n + 1, m + 1, (z + 1) % 3

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Files", "*.jpg")])
    if save_path:
        cv2.imwrite(save_path, img)
        log_message(f"Saved encrypted image: {save_path}", "success")
        os.system(f"start {save_path}")
    progress_bar.stop()


def decrypt_message():
    if img is None:
        log_message("No image loaded!", "error")
        return

    if pass_entry.get() != decrypt_pass_entry.get():
        log_message("Incorrect passcode!", "error")
        return

    n, m, z = 0, 0, 0
    decrypted_message = ""
    progress_bar.start()

    for i in range(len(msg_entry.get())):
        decrypted_message += c[img[n, m, z]]
        n, m, z = n + 1, m + 1, (z + 1) % 3

    log_message(f"Decrypted: {decrypted_message}", "success")
    progress_bar.stop()


def clear_all():
    msg_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    decrypt_pass_entry.delete(0, tk.END)
    img_label.config(image="")
    img_label.image = None
    log_console.delete(1.0, tk.END)
    global img, image_path
    img, image_path = None, ""


def log_message(msg, level="info"):
    colors = {"success": "#00FF00", "error": "#FF4444", "info": "#FFFFFF"}
    log_console.insert(tk.END, f"{msg}\n", level)
    log_console.tag_config(level, foreground=colors.get(level, "#FFFFFF"))
    log_console.see(tk.END)


def save_log():
    with open("steganography_log.txt", "w") as file:
        file.write(log_console.get(1.0, tk.END))
    log_message("Log saved to steganography_log.txt", "info")


def toggle_theme():
    if root["bg"] == "#222831":
        root.configure(bg="#f0f0f0")
        log_console.configure(bg="white", fg="black")
        for widget in root.winfo_children():
            widget.configure(bg="#f0f0f0", fg="black")
    else:
        root.configure(bg="#222831")
        log_console.configure(bg="#121212", fg="#00FF00")
        for widget in root.winfo_children():
            widget.configure(bg="#222831", fg="white")


# GUI Setup
root = tk.Tk()
root.title("Steganography Tool - Advanced")
root.geometry("700x600")
root.configure(bg="#222831")

# Header
Label(root, text="🕵️ Advanced Steganography Tool", font=("Helvetica", 18, "bold"), bg="#222831", fg="#00ADB5").pack(pady=10)

# Image Frame
img_label = Label(root, bg="#222831", relief=tk.SUNKEN)
img_label.place(x=20, y=60, width=200, height=200)

Button(root, text="Load Image", command=load_image, bg="#00ADB5", fg="white").place(x=240, y=60, width=150)

char_count_label = Label(root, text="Max Length: N/A", bg="#222831", fg="lightgreen")
char_count_label.place(x=240, y=95)

# Message & Password Inputs
Label(root, text="Secret Message:", bg="#222831", fg="white").place(x=20, y=270)
msg_entry = Entry(root, width=60)
msg_entry.place(x=20, y=290)
msg_entry.bind('<KeyRelease>', update_char_count)

Label(root, text="Encryption Passcode:", bg="#222831", fg="white").place(x=20, y=320)
pass_entry = Entry(root, width=60, show="*")
pass_entry.place(x=20, y=340)

Button(root, text="Encrypt & Save", command=encrypt_message, bg="#00ADB5", fg="white").place(x=20, y=370, width=150)

# Decrypt Section
Label(root, text="Decryption Passcode:", bg="#222831", fg="white").place(x=20, y=410)
decrypt_pass_entry = Entry(root, width=60, show="*")
decrypt_pass_entry.place(x=20, y=430)

Button(root, text="Decrypt", command=decrypt_message, bg="#FF6347", fg="white").place(x=20, y=460, width=150)
Button(root, text="Clear All", command=clear_all, bg="#FF4444", fg="white").place(x=180, y=460, width=100)

# Progress Bar
progress_bar = ttk.Progressbar(root, mode='indeterminate')
progress_bar.place(x=20, y=500, width=260)

# Log Console
log_console = Text(root, height=8, width=80, bg="#121212", fg="#00FF00", font=("Consolas", 10))
log_console.place(x=20, y=530)

# Save Log and Theme Toggle
Button(root, text="Save Log", command=save_log, bg="#00ADB5", fg="white").place(x=600, y=530, width=80)
Button(root, text="Toggle Theme", command=toggle_theme, bg="#555555", fg="white").place(x=600, y=560, width=80)

# Run GUI
root.mainloop()

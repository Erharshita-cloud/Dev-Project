from tkinter import *
from time import strftime
from PIL import Image, ImageTk  # For background image

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = Tk()
root.title("Digital Clock")

# Set window size
root.geometry("600x400")

# Load and place background image
bg_image = Image.open("bg.png")  # Replace with your image file
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create clock label
label = Label(root, font=('Arial', 50, 'bold'), bg='black', fg='cyan')
label.pack(pady=100)

time()
root.mainloop()

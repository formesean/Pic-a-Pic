import os
import random
import tkinter as tk
from tkinter import PhotoImage, Label, Button
from PIL import Image, ImageTk
from image_loader import load_images
import argparse

class PicAPic:
    def __init__(self, root, image_folder):
        self.root = root
        self.root.title("Pic-a-Pic") # Set window title
        self.root.geometry("700x550") # Set window size

        # Store the image folder path and Load images from it
        self.image_folder = image_folder
        self.image = load_images(self.image_folder)

        self.image_label = Label(root)
        self.image_label.pack(pady=20)

        self.show_button = Button(root, text="Kaboom!", command=self.show_random_image)
        self.show_button.pack(pady=10)

    def show_random_image(self):
        """Display a random image from the loaded images."""

        if self.image:
            random_image = random.choice(self.image)
            image_path = os.path.join(self.image_folder, random_image) # Construct the full image path

            image = Image.open(image_path)
            image = image.resize((450, 450))
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            self.image_label.config(text="No images found!")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pic-a-Pic")
    parser.add_argument("image_folder_path", type=str, help="Path to the folder")

    args = parser.parse_args()
    image_folder_path = args.image_folder_path

    window = tk.Tk()
    app = PicAPic(window, image_folder_path)
    window.mainloop()


import os

def load_images(image_folder):
    """Load all images from the specified folder."""
    supported_formats = ('.png', '.jpg', '.jpeg', '.gif')
    
    return [f for f in os.listdir(image_folder) if f.endswith(supported_formats)]


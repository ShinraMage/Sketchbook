import os
from PIL import Image

def convert_png_to_jpg(root_folder):
    # Walk through root_folder and its subdirectories.
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".png"):
                png_path = os.path.join(dirpath, filename)
                
                # Clip the first 30 characters from the filename
                new_filename = filename[:30]
                
                # Use the new_filename for the jpg_path
                jpg_path = os.path.join(dirpath, new_filename[:-4] + ".jpg")
                
                with Image.open(png_path) as img:
                    img = img.convert("RGBA")  # Convert the image to RGBA mode
                    data = img.getdata()
                    
                    # Create a new image with white background
                    new_img = Image.new("RGB", img.size, (0, 0, 0))
                    new_img.paste(img, mask=img.split()[3])  # Use the alpha channel as a mask
                    
                    new_img.save(jpg_path, "JPEG")

if __name__ == "__main__":
    root_folder = "./"
    convert_png_to_jpg(root_folder)

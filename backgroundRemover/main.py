from rembg import remove
from tkinter import Tk, filedialog
from PIL import Image
import os

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Choose a picture file",
    filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)

if file_path and file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
    print("Selected file:", file_path)

    file_name = os.path.basename(file_path)
    file_name_wo_ext = os.path.splitext(file_name)[0]
    output_name = file_name_wo_ext + "_output.png"

    with open(file_path, 'rb') as i:
        input_data = i.read()
        output_data = remove(input_data)

    with open(output_name, 'wb') as o:
        o.write(output_data)

    print("Background removed. New file:", output_name)
else:
    print("A valid picture file was not selected!")

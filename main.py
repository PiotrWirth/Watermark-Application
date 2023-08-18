import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

f_types = [('Jpg Files', '*.jpg')]
window = Tk()


def upload_file():
    global img, filename

    filename = askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    canvas = Canvas(window, width=img.width(), height=img.height())
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.grid(row=7, column=1)
    b2.config(state="normal")
    b3.config(state="normal")


def add_watermark(watermark):
    global image
    # make the image editable
    image = Image.open(filename)
    drawing = ImageDraw.Draw(image)
    # get text width and height
    text = f'©{watermark}'
    font = ImageFont.truetype("arial.ttf", 10)
    c_text = Image.new('RGB', (image.size), (0, 0, 0, 0))
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), text, font=font)
    c_text.putalpha(40)
    image.paste(c_text, mask=c_text)
    img.paste(image)


def save_image():
    rgb_im = image.convert('RGB')
    a = asksaveasfilename(title="Select file", filetypes=f_types)
    rgb_im.save(a)


window.title("Watermark App")
window.config(padx=50, pady=50)
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(window, text='Upload your image', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(window, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=1)

label_watermark = Label(text="Enter your watermark here")
label_watermark.grid(column=1, row=3)

entry_watermark = Entry(width=50)
entry_watermark.insert(END, string="@watermark")
entry_watermark.grid(column=1, row=4, sticky="ew")

b2 = tk.Button(window, text='Add Watermark',
               width=20, command=lambda: add_watermark(entry_watermark.get()), state="disabled")
b2.grid(row=5, column=1)


b3 = tk.Button(window, text='Save Image',
               width=20, command=lambda: save_image(), state="disabled")
b3.grid(row=6, column=1)


window.mainloop()

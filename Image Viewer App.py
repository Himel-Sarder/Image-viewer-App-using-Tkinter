from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")
root.maxsize(400, 400)

current_index = 0
image_paths = ["4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg"]
label = Label(root)
label.pack()

def show_image():
    if image_paths:
        image_path = image_paths[current_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        status_bar.config(text=f"{current_index + 1} of {len(image_paths)}")

# Show Developed by status
developed_by_label = Label(root, text="Developed by Himel Sarder", font=("Cooper Black", 10), fg="#B31942")
developed_by_label.pack(side="bottom")
def show_next_image():
    global current_index
    if image_paths:
        current_index = (current_index + 1) % len(image_paths)
        show_image()

def show_prev_image():
    global current_index
    if image_paths:
        current_index = (current_index - 1) % len(image_paths)
        show_image()

def exit_app():
    root.destroy()

# Create a frame to center the buttons
button_frame = Frame(root)
button_frame.pack()

prev_button = Button(button_frame, text="<< Previous", command=show_prev_image, bg="Pink")
prev_button.pack(side="left")

exit_button = Button(button_frame, text="Exit", command=exit_app, bg="Pink")
exit_button.pack(side="left", padx=10)

next_button = Button(button_frame, text="Next >>", command=show_next_image, bg="Pink")
next_button.pack(side="left")

# Status bar
status_bar = Label(root, text=f"{current_index + 1} of {len(image_paths)}", bd=1, relief="sunken", anchor="center")
status_bar.pack(side="bottom", fill="x")

show_image()
root.mainloop()

#Himel Sarder
#Dept. of CSE, BSFMSTU

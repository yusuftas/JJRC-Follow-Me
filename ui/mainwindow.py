import sys
import os


#relative_parent = os.path.join(os.getcwd(),'..')
SCRIPT_DIR = os.path.abspath(os.getcwd())
sys.path.append(SCRIPT_DIR)

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from Camera import camera

def camera_reader_proc(pipe):
    p_output, p_input = pipe

    class AppScreen:
        def __init__(self, window, window_title):
            self.window = window
            self.window.title(window_title)
            self.camera = camera.Camera(pipe)
            
            # Create a canvas with temporary size for now
            self.canvas = tkinter.Canvas(window, width = 640, height = 480)
            self.canvas.pack()

            self.delay = 15
            self.update()

            self.window.mainloop()

        def update(self):
            # Get a frame from the video source
            frame = self.camera.get_RGB_image()

            if frame is None:
                self.window.after(self.delay, self.update)
                return

            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

            self.window.after(self.delay, self.update)


    # Start the window
    AppScreen(tkinter.Tk(), "JJRC Follow me")  
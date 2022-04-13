import tkinter
import cv2


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source 
        
        # Create a canvas with temporary size for now
        self.canvas = tkinter.Canvas(window, width = 640, height = 480)
        self.canvas.pack()

        self.window.mainloop()

# Start the window
App(tkinter.Tk(), "JJRC Follow me")  
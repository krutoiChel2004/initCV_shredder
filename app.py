import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os

class WebcamApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        
        self.cap = cv2.VideoCapture(self.video_source)
        
        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        self.btn_snapshot = tk.Button(window, text="Сделать снимок", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
        
        self.update()
        
        self.window.mainloop()
        
    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)
        
    def snapshot(self):
        ret, frame = self.cap.read()
        if ret:
            files = os.listdir(path="frames")
            c = len(files)
            cv2.imwrite(f"frames\\f{c}.png", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print("Снимок сохранен")

# Создание экземпляра приложения
WebcamApp(tk.Tk(), "Вебкамера снимок")

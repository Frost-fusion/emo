import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}


class Display:
    def __init__(self, mod, video_source=0):
        global model
        model = mod
        self.appname = "emotion detection"
        self.window = Tk()
        self.window.title(self.appname)
        self.window['bg'] = 'black'
        self.video_source = video_source
        self.btn = Button(self.window,
                          text="Browse Files", width=20, bg="goldenrod2",
                          activebackground="red",
                          command=self.browseFiles)

        self.btn1 = Button(self.window,
                           text="Switch to Camera", width=20, bg="goldenrod2",
                           activebackground="red",
                           command=self.fun)
        self.vid = vidcapture(self.video_source)
        self.label = Label(self.window, text=self.appname, font=15,
                           bg='blue', fg='white').grid(row=0, column=0, columnspan=2)
        self.canvas = Canvas(self.window, width=self.vid.wid, height=self.vid.ht, bg="red")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.btn.grid(row=2, column=0)
        self.btn1.grid(row=2, column=1)

        self.update()
        self.window.mainloop()

    def update(self):
        istrue, frame = self.vid.getframe()
        if istrue:
            self.canvas.config(width=self.vid.wid, height=self.vid.ht)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.window.after(5, self.update)

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir="/")
        self.video_source = self.filename
        self.vid = vidcapture(self.video_source)

    def fun(self):
        self.vid = vidcapture(0)


class vidcapture:
    def __init__(self, video_source):
        self.cap = cv2.VideoCapture(video_source)
        self.wid = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.ht = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getframe(self):

        if self.cap.isOpened():
            res, frame = self.cap.read()
            if res:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces = face_detect.detectMultiScale(gray, 1.1, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    cropped = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                    prediction = model.predict(cropped)
                    label = int(np.argmax(prediction))
                    # cv2.putText(frame, emotion_dict[label], (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 4)
                    # cv2.putText(frame, str(prediction), (x-500, y+h), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
                    cv2.putText(frame, emotion_dict[label], (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255), 2, cv2.LINE_AA)
                return res, frame
            else:
                return res, None
        else:
            return None

    def __del__(self):
        self.cap.release()

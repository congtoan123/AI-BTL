import os
import tkinter as tk
import inspect
import check_camera
import Capture_Image
import Train_Image
import Recognize
CurDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

window = tk.Tk()
# helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")
dialog_title = 'QUIT'
dialog_text = 'Are you sure?'

# answer = messagebox.askquestion(dialog_title, dialog_text)

window.geometry('1450x750')
window.configure(background='light sky blue')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="ĐIỂM DANH VỚI NHẬN DIỆN KHUÔN MẶT", bg="gray67", fg="snow", width=70, height=3,
                   font=('times', 30))

message.place(x=0, y=20)

lbl = tk.Label(window, text="Nhập ID", width=20, height=2, fg="red", bg="pink1", font=('times', 15, ' bold '))
lbl.place(x=300, y=200)

txt = tk.Entry(window, width=20, bg="white", fg="red", font=('times', 15, ' bold '))
txt.place(x=600, y=215)

lbl2 = tk.Label(window, text="Nhập Tên", width=20, fg="red", bg="pink1", height=2, font=('times', 15, ' bold '))
lbl2.place(x=300, y=300)

txt2 = tk.Entry(window, width=20, bg="white", fg="red", font=('times', 15, ' bold '))
txt2.place(x=600, y=315)

lbl3 = tk.Label(window, text="Thông Báo : ", width=20, fg="red", bg="pink1", height=2,
                font=('times', 15, ' bold underline '))
lbl3.place(x=300, y=400)

message = tk.Label(window, text="", bg="white", fg="red", width=30, height=2, activebackground="pink1",
                   font=('times', 15, ' bold '))
message.place(x=600, y=400)

lbl3 = tk.Label(window, text="Trường Hợp Có Mặt : ", width=20, fg="red", bg="pink1", height=2,
                font=('times', 15, ' bold  underline'))
lbl3.place(x=300, y=650)

message2 = tk.Label(window, text="", fg="red", bg="white", activeforeground="green", width=30, height=2,
                    font=('times', 15, ' bold '))
message2.place(x=600, y=650)


def clear():
    txt.delete(0, 'end')
    res = ""
    message.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = ""
    message.configure(text=res)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def checkCamera():
    check_camera.camer()

def AutoMail():
    pass
def CaptureFaces():
    Id = (txt.get())
    name = (txt2.get())
    if (is_number(Id) and name.isalpha()):
        res=Capture_Image.takeImages(Id,name)
        message.configure(text=res)
    else:
        if (is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text=res)
        if (name.isalpha()):
            res = "Enter Numberic Id"
            message.configure(text=res)
def Trainimages():
    Train_Image.TrainImages()
    res = "Image Trained"
    message.configure(text=res)

def RecognizeFaces():
    res=Recognize.recognize_attendence()
    message2.configure(text=res)

clearButton = tk.Button(window, text="Clear", command=clear, fg="red", bg="pink1", width=15, height=2,
                        activebackground="Red", font=('times', 15, ' bold '))
clearButton.place(x=850, y=200)
clearButton2 = tk.Button(window, text="Clear", command=clear2, fg="red", bg="pink1", width=15, height=2,
                         activebackground="Red", font=('times', 15, ' bold '))
clearButton2.place(x=850, y=300)
takeImg = tk.Button(window, text="Lấy Ảnh Mẫu", command=CaptureFaces, fg="red", bg="pink1", width=15, height=2,
                    activebackground="Red", font=('times', 15, ' bold '))
takeImg.place(x=100, y=500)
trainImg = tk.Button(window, text="Train Ảnh", command=Trainimages, fg="red", bg="pink1", width=15, height=2,
                     activebackground="Red", font=('times', 15, ' bold '))
trainImg.place(x=300, y=500)
trackImg = tk.Button(window, text="Nhận Diện", command=RecognizeFaces, fg="red", bg="pink1", width=15, height=2,
                     activebackground="Red", font=('times', 15, ' bold '))
trackImg.place(x=500, y=500)
CheckCam = tk.Button(window, text="CheckCam", command=checkCamera, fg="red", bg="pink1", width=15, height=2,
                     activebackground="Red", font=('times', 15, ' bold '))
CheckCam.place(x=700,y=500)
CheckCam = tk.Button(window, text="Mail", command=AutoMail, fg="red", bg="pink1", width=15, height=2,
                     activebackground="Red", font=('times', 15, ' bold '))
CheckCam.place(x=900,y=500)
quitWindow = tk.Button(window, text="Thoát", command=window.destroy, fg="red", bg="pink1", width=15, height=2,
                       activebackground="Red", font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,
                    font=('times', 30, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Developed by N16", "", "TEAM", "AI")
copyWrite.configure(state="disabled", fg="red")
copyWrite.pack(side="left")
copyWrite.place(x=800, y=750)

window.mainloop()
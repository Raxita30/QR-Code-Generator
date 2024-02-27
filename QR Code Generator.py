from tkinter import *
import pyqrcode

tk = Tk()
tk.title("QR Code")


def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        output.config(text="Oops Enter the URL")
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())


lbl = Label(tk,text="Enter message or URL")
lbl.pack()

user_input = StringVar()
entry = Entry(tk,textvariable = user_input)
entry.pack(padx=10)


button = Button(tk,text = "Generate QR",width=15,command = generate_QR)
button.pack(pady=10)

img_lbl = Label(tk)
img_lbl.pack()
output = Label(tk)
output.pack()
 
tk.mainloop()


from tkinter import *
from cv2 import rotate
import rotatescreen

def Screen_rotation(enter):
    screen = rotatescreen.get_primary_display()
    if enter == "up":
        screen.set_landscape()
    elif enter == "right":
        screen.set_portrait_flipped()
    elif enter =="doen":
        screen.set_landscape_flipped()
    elif enter =="left":
        screen.set_portrait_flipped()             

root = Tk()
root.title("Screen Rotation")
root.configure(bg="#54c5d1")
root.geometry("500x500")
root.resizable(False,False)

Photo = PhotoImage(file="background.png")
myimage = Label(image=Photo)
myimage.pack(padx=2,pady=2)



Button(root,text="up",command=lambda:Screen_rotation("up"),
       bg="white",font="arial 18",width=5).place(x=200,y=50)


Button(root,text="right",command=lambda:Screen_rotation("right"),
       bg="white",font="arial 18",width=5).place(x=402,y=230)


Button(root,text="left",command=lambda:Screen_rotation("left"),
       bg="white",font="arial 18",width=5).place(x=20,y=230)


Button(root,text="doen",command=lambda:Screen_rotation("doen"),
       bg="white",font="arial 18",width=5).place(x=220,y=400)







root.mainloop()
from tkinter import *
import string;from random import choice
def gen():
  entry1.delete(0,END)
  fkey=[]
  for x in range(9):
      key = list(string.ascii_letters+string.digits)
      key = choice(key)
      fkey.append(key)
      "".join(fkey)
      entry1.insert(INSERT,fkey)
root=Tk()
root.title("KeyGen")
root.geometry("200x45")
entry1=Entry(root,width=15)
entry1.place(x=2,y=3)
button1=Button(root,text="gen",command=gen)
button1.place(x=140,y=0)
root.mainloop()

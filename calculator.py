from tkinter import *


def clickbtn(event):
    global entry
    value = event.widget.cget("text")
    if value == "=":
        if entry.get().isdigit():
            val = int(entry.get())
            entry.set(val)
            entryValue.update()
        else:
            result = eval(entry.get())
            entry.set(result)
            entryValue.update()
    elif value == "c":
        entry.set("")
        entryValue.update()
    elif value == "%":
        try:
            entry.get().index(value)
        except:
            entry.set(entry.get() + str(value))
            entryValue.update()
        else:
            pass
    elif value == "+":
        try:
            entry.get().index(value)
        except:
            entry.set(entry.get() + str(value))
            entryValue.update()
        else:
            pass
    elif value == "-":
        try:
            entry.get().index(value)
        except:
            entry.set(entry.get() + str(value))
            entryValue.update()
        else:
            pass
    elif value == "/":
        try:
            entry.get().index(value)
        except:
            entry.set(entry.get() + str(value))
            entryValue.update()
        else:
            pass
    elif value == "*":
        try:
            entry.get().index(value)
        except:
            entry.set(entry.get() + str(value))
            entryValue.update()
        else:
            pass
    else:
        entry.set(entry.get() + str(value))
        entryValue.update()

root = Tk()
root.geometry("300x400")

create_frame_entry = Frame(root, bg="gray")
create_frame_entry.pack()
entry = StringVar()
entry.set("")
entryValue = Entry(create_frame_entry,textvar=entry,font="opensans 45 bold",state="disable")
entryValue.pack()

createingList = ['+', '/', '=', 'c', 1, 2, 3, 4, 5, 6,  7, 8, 9, 0, '%',  '*', ]
j = 1
createbtn = list(range(len(createingList)))
print(createbtn)
create_frame_sc = Frame(root, bg="gray")
for ls in createingList:

    createbtn = Button(create_frame_sc, text=ls,padx=20,pady=20)
    createbtn.bind('<Button-1>',clickbtn)
    createbtn.pack(side=LEFT)
    if j % 4 == 0:
        if j != 0:
            print(j)
            create_frame_sc.pack()
            create_frame_sc = Frame(root, bg="gray")
    j = j + 1

root.mainloop()
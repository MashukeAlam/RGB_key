from tkinter import *

import keyboard

import threading
import sys
import random


color = ["#FF0000", "#00FFFF", "#00FF00", "#FF00FF", "#FFA500", "#000"]

key = ""
curr = ""
change = False
blocked_keys = ['', 'enter', 'shift', 'tab', 'ctrl', 'alt']
def get_key():
    global key, curr, change
    while True:

        key = keyboard.read_key()
        if key not in blocked_keys:
            curr = key
            change = True



kb_thread = threading.Thread(target=get_key)

root = Tk()
# root.pack(fill=BOTH, expand=1)cdfsasdawweqqqq
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
print(height, width)
root.geometry("180x80+1300+670")
root.configure(bg="black")
root.wm_attributes("-alpha", 0.35)
root.attributes('-topmost', True)
root.update()
c = Canvas(root, width=180, height=80)
c.configure(bg="black")
c.create_text(75, 40, anchor=W, font=("Monaco", 45), fill="#000",
            text="A")
c.pack(fill=BOTH, expand=1)
root.overrideredirect(1)
kb_thread.daemon = True
kb_thread.start()

t = 0
while True:

    if(curr == "esc"):
        break
    


    # print(key)

    if change:
        c.delete("all")
        c.create_text(75, 40, anchor=W, font=("Monaco", 45), fill=color[random.randint(0, len(color)) - 1],
                    text=curr)
    change = False
        

    # print("aa")
    root.update_idletasks()
    root.update()


if True:
    print("here")
    root.destroy()

    print(threading.active_count())
    try:
        print(blocked_keys)
        sys.exit(0)
    except:
        print("notworking")











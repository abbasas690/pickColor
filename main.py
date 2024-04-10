from PIL import ImageGrab
from pynput import mouse
import colorsys

import time
import tkinter as tk
import tkinter.ttk as ttk
def rgb_to_hex(pixel):
    r,g,b = pixel
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

pixel=[]
with mouse.Events() as e:
    for x in e:
        try:
            if x.button == mouse.Button.left:
                data=ImageGrab.grab()
                pixel=data.getpixel((x.x,x.y))
                print("pixel",pixel)
            if x.button == mouse.Button.right:
                break
            
        except: pass
        finally:
            data=ImageGrab.grab()
            pixel=data.getpixel((x.x,x.y))
            print("pixel",pixel)
            print("TT",type(pixel))

window = tk.Tk(screenName="pick color")
tk.Label(window, text=str(pixel),background= rgb_to_hex(pixel) ).grid(row=0,column=0)
print("after the ex: ",pixel)
# start the listener
# print("starting the mouse listener, will be active for 5 seconds...")
# time.sleep(5)
window.mainloop()
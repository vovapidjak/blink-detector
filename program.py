# importing tkinter for gui
import tkinter as tk
import time
from blink import blinkDetector
# creating window
window = tk.Tk()

# setting attribute
window.attributes('-fullscreen', True)
window.title("Geeks For Geeks")

label1 = tk.Label(window, text = "ЭТО АКТИВНОЕ ОКНО", font="arial 72")
label1.pack()

window.update()

if blinkDetector():
    window.destroy()





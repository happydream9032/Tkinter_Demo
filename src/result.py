import tkinter as tk

text = None
def draw_Dialog(type):
    #Create a Label in New windo
    root = tk.Tk()
    root.geometry("650x300")
    root.resizable(False, False)
    if type == 1:
        root.title("Image Conversion")
    elif type ==2:
        root.title("Image Rename")
    elif type == 3:
        root.title("Image Download")


    global text
    text = tk.Text(root)
    text.pack()

def add_result(value):
    global text
    #text.delete(1.0, "END")
    real_value = value + "\n"
    text.insert(tk.END, real_value)

from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *
from tkinter.messagebox import showwarning
from functools import partial
from PIL import Image, ImageTk
import subprocess

from converter import convert_func
from task1 import rename_func
from main import downloader_func

# Root window
root = tk.Tk()
root.title('Image works')
root.resizable(False, False)
root.geometry('470x670')

icon = tk.PhotoImage(file="Capture.PNG")
# Set it as the window icon.
root.iconphoto(True, icon)

#action party of first function
def first_open_file_select():
    file_name1 = fd.askdirectory()
    # read the text file and show its content on the Text
    first_file_path.set(file_name1)

def first_orgfolder_select():
    org_folder1 = fd.askdirectory()
    # read the text file and show its content on the Text
    first_origin_path.set(org_folder1)

def selection():
    selection = str(radio.get())
    if selection == '1':
        str_radio.set('Y')
    elif selection == '2':
        str_radio.set('N') 

def first_action_select(first_file_path, str_radio, first_origin_path):
    first_file_path_str = (first_file_path.get())
    str_radio_value = (str_radio.get())
    first_origin_path_str = (first_origin_path.get())

    if first_file_path_str != '' and first_origin_path_str != '' and str_radio_value != '':
        convert_func(first_file_path_str, first_origin_path_str, str_radio_value)
    else:
        showwarning(
            title='Input Warning',
            message='Please input all data correctly.'
        )

# action party of second function
def second_excel_file_select():
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    # show the open file dialog
    excel_name2 = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    # read the text file and show its content on the Text
    second_excel_path.set(excel_name2)

def second_orgfolder_select():
    org_folder2 = fd.askdirectory()
    # read the text file and show its content on the Text
    second_image_path.set(org_folder2)

def second_disfolder_select():
    dis_folder2 = fd.askdirectory()
    # read the text file and show its content on the Text
    second_folder_path.set(dis_folder2)

def second_convert_select(second_excel_path, second_image_path, second_folder_path):
    second_excel_path_str = (second_excel_path.get())
    second_image_path_str = (second_image_path.get())
    second_folder_path_str = (second_folder_path.get())
    if second_folder_path_str != '' and second_image_path_str != '' and second_excel_path_str != '' :
        rename_func(second_excel_path_str, second_image_path_str, second_folder_path_str )
    else:
        showwarning(
            title='Input Warning',
            message='Please input all data correctly.'
        )

# action party of third function
def third_excel_file_select():
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )
    # show the open file dialog
    excel_name3 = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    # read the text file and show its content on the Text
    third_excel_path.set(excel_name3)

def third_disfolder_select():
    org_folder3 = fd.askdirectory()
    # read the text file and show its content on the Text
    third_des_path.set(org_folder3)

def third_download_select(third_excel_path, third_des_path):
    third_excel_path_str = (third_excel_path.get())
    third_des_path_str = (third_des_path.get())
    if third_excel_path_str != "" and third_des_path_str != "":
        downloader_func(third_excel_path_str, third_des_path_str)
    else:
        showwarning(
            title='Input Warning',
            message='Please input all data correctly.'
        )
#action party of insert to text

first_file_path = tk.StringVar()
first_disfolder_path = tk.StringVar()
first_origin_path = tk.StringVar()
second_folder_path = tk.StringVar()
second_excel_path = tk.StringVar()
second_image_path = tk.StringVar()
third_excel_path = tk.StringVar()
third_des_path = tk.StringVar()

radio = IntVar()
str_radio = tk.StringVar()


# --Ui for first task---
first_label_frame = Frame(root,width=500, height=180, highlightbackground='black',highlightthicknes=2)
first_label_frame.grid(row=0,column=0,padx=10,pady=2,ipadx=5,ipady=5, sticky='w')

first_task_label = tk.Label(first_label_frame, text="Image Conversion to JPG", fg="blue", font=("Arial", 15)).grid(row=1, column=0, pady = 5, sticky='w')

first_label1 = tk.Label(first_label_frame, text="Select Folder of Original Images to Convert...").grid(row=2, column=0, sticky='w', padx = 10)
first_file_entry = ttk.Entry(first_label_frame, textvariable = first_file_path, width= 55).grid(row=3, column=0, sticky='w', padx = 10)
# open file button
first_open_file_button = ttk.Button(
    first_label_frame,
    text='Select Folder',
    command=first_open_file_select
)
first_open_file_button.grid(column=2, row=3, sticky='w')

first_label2 = tk.Label(first_label_frame, text="Select Destination Folder...").grid(row=4, column=0, sticky='w', padx = 10)
first_orgfile_entry = ttk.Entry(first_label_frame, textvariable = first_origin_path, width= 55).grid(row=5, column=0, sticky='w', padx = 10)
# open file button
first_open_orgfile_button = ttk.Button(
    first_label_frame,
    text='Select Folder',
    command=first_orgfolder_select
)
first_open_orgfile_button.grid(column=2, row=5, sticky='w')

first_sub_frame = Frame(first_label_frame)
first_sub_frame.grid(row=6,column=0,padx=5,pady = 5, sticky='w')

first_label3 = tk.Label(first_sub_frame, text="Delete Original Images?").grid(row=0, column=0, sticky='w', padx = 5)

first_radio_yes = Radiobutton(first_sub_frame, text="Yes", variable=radio, value=1,  command=selection).grid(column=1, row=0, sticky='w')
first_radio_no = Radiobutton(first_sub_frame, text="No", variable=radio, value=2,  command=selection).grid(column=2, row=0, sticky='w') 

first_action_select = partial(first_action_select, first_file_path, str_radio, first_origin_path)
first_convert_button = ttk.Button(
    first_label_frame,
    text='Convert',
    command=first_action_select
).grid(column=2, pady = 10, row=6, sticky='w')

# --Ui for second task---
second_label_frame = Frame(root,width=500, height=180, highlightbackground='black',highlightthicknes=2)
second_label_frame.grid(row=1,column=0,padx=10,pady=2,ipadx=5,ipady=5, sticky='w')

second_task_label = tk.Label(second_label_frame, text="Rename Images", fg="blue", font=("Arial", 15)).grid(row=8, column=0, pady = 10, sticky='w')
second_label1 = tk.Label(second_label_frame, text="Select .xlsx File (Column A; Original, Column B, New)").grid(row=9, column=0, sticky='w', padx = 10)
second_excelfile_entry = ttk.Entry(second_label_frame, textvariable = second_excel_path, width= 55).grid(row=10, column=0, padx = 10, sticky='w')
# open file button
second_open_excelfile_button = ttk.Button(
    second_label_frame,
    text='Select File',
    command=second_excel_file_select
)
second_open_excelfile_button.grid(column=1, row=10, sticky='w')
second_label2 = tk.Label(second_label_frame, text="Select Folder of Original Images to Rename...").grid(row=11, column=0, sticky='w', padx = 10)
second_image_entry = ttk.Entry(second_label_frame, textvariable = second_image_path, width= 55).grid(row=12, column=0, padx = 10, sticky='w')
# open file button
second_open_image_button = ttk.Button(
    second_label_frame,
    text='Select Folder',
    command=second_orgfolder_select
)
second_open_image_button.grid(column=1, row=12, sticky='w')

second_label3 = tk.Label(second_label_frame, text="Select Destination Folder...").grid(row=13, column=0, sticky='w', padx = 10)
second_dirfile_entry = ttk.Entry(second_label_frame, textvariable = second_folder_path, width= 55).grid(row=14, column=0, padx = 10, sticky='w')
# open file button
second_open_dirfile_button = ttk.Button(
    second_label_frame,
    text='Select Folder',
    command=second_disfolder_select
)
second_open_dirfile_button.grid(column=1, row=14, sticky='w')

second_convert_select = partial(second_convert_select, second_excel_path, second_image_path, second_folder_path)
second_convert_button = ttk.Button(
    second_label_frame,
    text='Rename',
    command=second_convert_select
).grid(column=1, row=15, sticky='w', pady = 10)

#-- Ui for third task
third_label_frame = Frame(root,width=500, height=180, highlightbackground='black',highlightthicknes=2)
third_label_frame.grid(row=2,column=0,padx=10,pady=2,ipadx=5,ipady=5, sticky='w')

third_task_label = tk.Label(third_label_frame, text="Image Download and Rename", fg="blue", font=("Arial", 15)).grid(row=8, column=0, pady = 10, sticky='w')
third_label1 = tk.Label(third_label_frame, text="Select .xlsx File (Column A; URLs, Column B; New File Name)").grid(row=17, column=0, sticky='w', padx = 10)

third_excelfile_entry = ttk.Entry(third_label_frame, textvariable = third_excel_path, width= 55).grid(row=18, column=0, padx = 10, sticky='w')
# open file button
third_open_excelfile_button = ttk.Button(
    third_label_frame,
    text='Select File',
    command=third_excel_file_select
)
third_open_excelfile_button.grid(column=1, row=18, sticky='w')

third_label2 = tk.Label(third_label_frame, text="Select Destination Folder...").grid(row=19, column=0, sticky='w', padx = 10)
third_image_entry = ttk.Entry(third_label_frame, textvariable = third_des_path, width= 55).grid(row=20, column=0, padx = 10, sticky='w')
# open file button
third_open_image_button = ttk.Button(
    third_label_frame,
    text='Select Folder',
    command=third_disfolder_select
)
third_open_image_button.grid(column=1, row=20, sticky='w')

third_download_select = partial(third_download_select, third_excel_path, third_des_path)
third_download_button = ttk.Button(
    third_label_frame,
    text='Download',
    command=third_download_select
).grid(column=1, row=21, sticky='w', pady = 10)

root.mainloop()

import logging
from pathlib import Path
from sys import argv
import tkinter as tk
import json
import result
#from popup import main as m
#from popup import add_result

try:
    from xlsx_read import get_dict_from_excel
except ModuleNotFoundError:
    print('Please ensure that the xlsx_read.py file is in the same directory as this script')
    result.add_result('Please ensure that the xlsx_read.py file is in the same directory as this script')
    input('Press enter to exit...')
    exit()
    
try:
    from renaming import change_file_name
except ModuleNotFoundError:
    print('Please ensure that the renaming.py file is in the same directory as this script')
    result.add_result('Please ensure that the renaming.py file is in the same directory as this script')
    input('Press enter to exit...')
    exit()

# check if the user wants to see the debug messages
if len(argv) > 2:
    if argv[1] == '-d':
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

def check_if_path_exists(file_path:Path):
    if file_path.exists():
        return True
    else:
        return False
    
def main(input_excel_file_name:str,
         images_folder_name:str,
         dest_folder_name:str
         ) -> None:
    
    logging.debug(f'\ncurrent working directory is {Path.cwd()}\n')
    
    # checking if the input excel file and the images folder exist in the current working directory
    input_excel_file_path = Path.cwd() / input_excel_file_name
    logging.debug(f'\ninput_excel_file_path: {input_excel_file_path}\n')
    excel_file_exists = check_if_path_exists(input_excel_file_path)
    if excel_file_exists:
        pass
    else:
        raise FileNotFoundError(f'The file {input_excel_file_name} does not exist in the current working directory')
    
    images_folder_path = Path.cwd() / images_folder_name
    logging.debug(f'\nimages input folder is {images_folder_path}\n')
    images_folder_exists = check_if_path_exists(images_folder_path)
    if images_folder_exists:
        pass
    else:
        raise NotADirectoryError(f'The folder {images_folder_name} does not exist in the current working directory')
    
    dest_folder_path = Path.cwd() / dest_folder_name
    dest_folder_exists = check_if_path_exists(dest_folder_path)
    if dest_folder_exists:
        pass
    else:
        logging.debug(f'\ncreating the destination folder {dest_folder_path}\n')
        dest_folder_path.mkdir()
    
    # get the dictionary from the excel file
    excel_dict = get_dict_from_excel(input_excel_file_path)
    logging.debug(excel_dict)
    
    for old_name, old_file_ext, new_name in zip(excel_dict['old_name'], excel_dict['old_file_ext'], excel_dict['new_name']):
        change_status_tup = change_file_name(org_directory=images_folder_path,
                                             dest_directory=dest_folder_path,
                                             old_name=old_name,
                                             old_file_ext=old_file_ext,
                                             new_name=new_name)
        print(change_status_tup[1])
        result.add_result(json.dumps(change_status_tup[1]))

def rename_func(input_excel_file_name, images_folder_name, dest_folder_name):
    result.draw_Dialog()
    print('-'*50)
    result.add_result('---------------------------------------')
    print('Please ensure that the input excel file and the images folder are in the same directory as this script')
    result.add_result('Please ensure that the input excel file and the images folder are in the same directory as this script')
    print('-'*50,'\n')
    result.add_result('----------------------------------------')
#    input_excel_file_name = input('Enter the name of the excel file: ')
#    images_folder_name = input('Enter the name of folder containing all the images: ')
#    dest_folder_name = input('Enter the name of the destination folder: ')
    main(input_excel_file_name=input_excel_file_name,
         images_folder_name=images_folder_name,
         dest_folder_name=dest_folder_name)


#if __name__ == '__main__':


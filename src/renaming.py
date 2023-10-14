from pathlib import Path
from shutil import copyfile
from typing import Dict, Union, Tuple

def check_file_exists(directory:Path, filename:str, file_ext:str) -> bool:
    """
    ## Usage
    This function will check if a file exists in a directory.
    
    ## Parameters
    1. directory: `Path` -> the directory to check
    2. filename: `str` -> the filename to check
    3. file_ext: `str` -> the file extension
    
    ## Returns
    `bool` -> `True` if the file exists, `False` otherwise
    """
    return (directory / (filename + '.' + file_ext)).exists()

def change_file_name(org_directory:Path,
                     dest_directory:Path,
                     old_name:str,
                     old_file_ext:str,
                     new_name:str
                     ) -> Tuple[int,Dict[str, str]]:
    """
    ## Usage
    This function will copy an image file from one directory to another, and rename it, only if the following conditions are met:
    1. the old file exists
    2. the new file does not exist (in `.jpg` format or in the `old file extension` format)
    
    ## Parameters
    1. org_directory: `Path` -> the directory that contains the old file
    2. dest_directory: `Path` -> the directory that will contain the new file
    3. old_name: `str` -> the old filename
    4. old_file_ext: `str` -> the old file extension
    5. new_name: `str` -> the new filename
    
    ## Returns
    Tuple[int,Dict[str, str]] -> a tuple of two elements:
    1. `int` -> the status code of the renaming (200 if successful, 400 otherwise)
    2. `Dict[str, str]` -> a dictionary with the following keys:
        1. `str` -> the old filename
        2. `str` -> the response message from the func
    """
    old_file_exists = check_file_exists(org_directory, old_name, old_file_ext)
    new_file_exists = check_file_exists(dest_directory, new_name, 'jpg') or check_file_exists(dest_directory, new_name, old_file_ext)
    if old_file_exists:
        if new_file_exists:
            return (400, {f'{old_name}.{old_file_ext}': f'could not rename file because new file already exists with name {new_name}'})
        else:
            old_file_path = org_directory / (old_name + '.' + old_file_ext)
            new_file_path = dest_directory / (new_name + '.' + old_file_ext)
            copyfile(src=old_file_path, dst=new_file_path)
            new_file_path.rename(dest_directory / (new_name + '.' + old_file_ext))
            return (200, {f'{old_name}.{old_file_ext}': f'file was successfully renamed to {new_name}.{old_file_ext}'})
    else:
        return (404, {f'{old_name}.{old_file_ext}': 'file does not exist'})
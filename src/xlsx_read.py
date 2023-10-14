from pylightxl import readxl
from pathlib import Path
from typing import List, Dict, Union, Tuple

def split_filename_and_extension(filename: str,
                                 return_ext:bool=True
                                 ) -> Union[ str, Tuple[str,str] ]:
    """
    # Usage
    This function will split a filename into a tuple of two elements:
    1. The filename without the extension
    2. The extension of the file including the period (.) -> optional
    
    # Parameters
    1. filename: str
        The filename to split
    2. return_ext: bool
        Whether to return the extension or not. Default is `True`.
    
    # Returns
    1. `Union[ str, Tuple[str,str] ]`
        If `return_ext` is `True`, then a `tuple` of two strings is returned.
        If `return_ext` is `False`, then a `string` is returned.
        
    # Edge Cases
    This function will misbehave if the filename period in it but doesn't have an extension.\n
    Examples:
    1. correct: `some.file.name.jpg` -> `('some.file.name', 'jpg')`
    2. incorrect: `some.file.name` -> `('some.file', 'name')`
    """
    filename_split = filename.split('.')
    
    # if there is no extension
    if len(filename_split) == 1:
        return (filename, '') if return_ext else filename
    ext = filename_split[-1]
    name = '.'.join(filename_split[:-1])
    return (name, ext) if return_ext else name

def parse_columns(old_names:List[str], new_names:List[str]) -> Dict[str, Tuple[str]]: 
    """
    ## Usage
    this function will parse the columns of the excel file into a dictionary of tuples.
    
    ## Parameters
    1. old_names: `List[str]`
    2. new_names: `List[str]`
    
    ## Returns
    `Dict[str, Tuple[str]]` \n
    a dictionary of tuples with the following keys:
    1. old_name: `Tuple[str]` -> the old name of the file
    2. old_file_ext: `Tuple[str]` -> the extension of the old file
        -> this is done because further on in the code, the extension will be changed to `.jpg` so this might be useful
    3. new_name: `Tuple[str]` -> the new name of the file
    """
    
    # remove the first element of the list (the header in the excel file)
    old_names.pop(0)
    new_names.pop(0)
    
    # instantiate the dictionary
    col_dict = dict()
    
    # split the old filename into two separate tuples of strings (filename, extension)
    old_names, file_exts = zip(*[split_filename_and_extension(old_name) for old_name in old_names])
    # get the new filename without the extension (because it'll all be `.jpg` anyway)
    new_names = tuple([split_filename_and_extension(new_name, return_ext=False) for new_name in new_names])
    
    # update the dictionary
    col_dict.update({'old_name':old_names})
    col_dict.update({'old_file_ext':file_exts})
    col_dict.update({'new_name':new_names})
    return col_dict

def get_dict_from_excel(file_path:Path) -> Dict[str, Tuple[str]]:
    """
    ## Usage
    This function will read the excel file and return a dictionary of tuples.
    
    ## Parameters
    file_path: `Path` -> the path to the excel file
    
    ## Returns
    `Dict[str, Tuple[str]]` \n
    a dict containing the following keys:
    1. old_name: `Tuple[str]` -> the old name of the file
    2. old_file_ext: `Tuple[str]` -> the extension of the old file
        -> this is done because further on in the code, the extension will be changed to `.jpg` so this might be useful
    3. new_name: `Tuple[str]` -> the new name of the file
    
    ## Edge Cases
    this function will misbehave if the excel file does not follow this structure:
    1. the first worksheet is the only worksheet
    2. the first column is the old names column
    3. the second column is the new names column
    4. the first row is the header
    5. there are no empty cells in the columns
    6. the file extension is not included in the old names column
    7. the file extension is not included in the new names column
    """
    
    # read the excel file into a database using pylightxl
    xl_db = readxl(fn=file_path)
    # get the name of the first worksheet
    sheet1_name = xl_db.ws_names[0]
    # get the columns of the first worksheet
    old_names_col, new_names_col = xl_db.ws(ws=sheet1_name).cols
    # transforming both lists to list of strings
    old_names_col = [str(x) for x in old_names_col]
    new_names_col = [str(x) for x in new_names_col]
    return parse_columns(old_names_col, new_names_col)
from pylightxl import readxl, Database as PylightDatabase
from pathlib import Path
import result

class MoreThanOneSheetError(Exception):
    pass

class FileNot_XLSX_Error(Exception):
    pass

def get_pylight_database(input_file_path_str:str) -> PylightDatabase:
    path_file = Path(input_file_path_str)
    if not(path_file.exists()):
        raise FileNotFoundError(f'File not found at: {input_file_path_str}')
    if path_file.suffix != '.xlsx':
        raise FileNot_XLSX_Error(f'File extension must be .xlsx')
    pylight_db = readxl(path_file)
    ws_names = pylight_db.ws_names
    if len(ws_names) > 1:
        raise MoreThanOneSheetError(f'File must contain only one sheet')
    return pylight_db

def read_data_from_xlsx(pylight_db:PylightDatabase) -> dict:
    ws_name = pylight_db.ws_names[0]
    urls = [row[0] for row in pylight_db.ws(ws_name).rows]
    image_names = [row[1] for row in pylight_db.ws(ws_name).rows]
    dict_returned = dict(zip(image_names[1:],urls[1:]))
    return dict_returned
if __name__ == '__main__':
    pylight_db = get_pylight_database('source/image-urls.xlsx')
    images_dict = read_data_from_xlsx(pylight_db)
    print(images_dict)
    result.add_result(images_dict)

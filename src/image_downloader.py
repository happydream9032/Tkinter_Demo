from requests import get, Response
from pathlib import Path
from typing import Tuple

class imageAlreadyExistsError(Exception):
    pass

class cantDownloadImage(Exception):
    pass

def get_save_directory(save_dir_str:str) -> Path:
    """
    ## Usage
    This function takes a string for the saving directory, creates the directory if it doesn't exist, and returns a Path object for the directory.
    
    ## Parameters
    save_dir_str: str
        The string for the saving directory.
    
    ## Returns
    `Path` object for the saving directory.
    """
    save_dir = Path(save_dir_str)
    if not(save_dir.exists()):
        save_dir.mkdir(parents=True, exist_ok=True)
    return save_dir

def check_image_exists(save_dir:Path, image_name:str) -> bool:
    """
    ## Usage
    This function simply checks if the image already exists in the saving directory. If it does, it raises an error. If it doesn't, it returns False.
    
    ## Parameters
    1. save_dir: `Path` object
        The saving directory.
    2. image_name: str
        The name of the image (with the file format suffix).
    
    ## Returns
    `False` if the image doesn't exist.
    
    ## Raises
    `imageAlreadyExistsError` &rarr; if the image already exists.
    """
    image_path = save_dir / image_name
    if image_path.exists():
        raise imageAlreadyExistsError(f'Image already exists at: {image_path}')
    return False

def download_image(image_url:str) -> Tuple[int,Response|None]:
    """
    ## Usage
    This function downloads the image from the URL and returns the response.
    
    ## Parameters
    1. image_url: str
        The URL of the image.
    
    ## Returns
    `Response` object from the `requests` library.
    
    ## Raises
    `cantDownloadImage` &rarr; if the image can't be downloaded.
    """
    response = get(image_url)
    if response.status_code == 200:
        return (200,response)
    elif response.status_code == 403:
        return (403,None)
    else:
        raise cantDownloadImage(f'Error downloading image from: {image_url}, status code: {response.status_code}')

def touch_image_file(save_dir:Path, image_name:str) -> Path:
    """
    ## Usage
    This function creates the image file in the saving directory.
    
    ## Parameters
    1. save_dir: `Path` object
        The saving directory.
    2. image_name: str
        The name of the image (with the file format suffix).
    
    ## Returns
    `Path` object for the image file.
    """
    image_path = save_dir / image_name
    image_path.touch()
    return image_path

def save_image_to_file(response:Response, image_path:Path) -> None:
    """
    ## Usage
    This function saves the image to the image file.
    
    ## Parameters
    1. response: `Response` object
        The response from the `requests` library.
    2. image_path: `Path` object
        The path to the image file (should already be created).
    
    ## Returns
    None
    """
    with open(image_path, 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    save_dir = get_save_directory('images_test')
    image_name = 'test.jpg'
    image_url = 'https://unitedmotorproducts.com/wp-content/uploads/2021/04/CAM-161_1_eeS90bw3j.jpg'
    check_image_exists(save_dir, image_name)
    get_response = download_image(image_url)
    touch_image_file(save_dir, image_name)
    save_image_to_file(get_response, save_dir / image_name)
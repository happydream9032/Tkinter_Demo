from PIL import Image, UnidentifiedImageError
from pathlib import Path
from os import remove as remove_file
import logging
from sys import argv
from termcolor import colored
from tqdm import tqdm
#from tqdm.gui import tqdm
import result

class AlreadyJpgError(Exception):
    pass

class JpgConverter:

    def __init__(self,
                 source_img_path:Path,
                 dest_dir:Path=None,
                 delete_org:bool=False
                 ) -> None:
        try:
            #logging.debug(f'source_img_path: {colored(source_img_path, "blue")}')
            self.image = Image.open(source_img_path)
            #logging.debug(f'image.format: {colored(self.image.format,"green")}')
            # checking if the source image is already a jpg
            if (self.image.format == 'JPEG') and (dest_dir is None):
                raise AlreadyJpgError(f'image is already a jpg at this path: {colored(source_img_path,"blue")}')

            # getting the original image name without the suffix
            image_name_no_suffix = source_img_path.stem
            #logging.debug(f'image_name_no_suffix: {image_name_no_suffix}')
            # setting the destination dir to the source image dir if not specified
            if not dest_dir:
                dest_dir = source_img_path.parent
            else:
                dest_dir = Path().cwd() / dest_dir
            dest_path_parent = dest_dir
            dest_path = dest_dir / f'{image_name_no_suffix}.jpg'
            #logging.debug(f'dest_path: {dest_path}')

            # checking if there is already a jpg file with the same name in the destination directory
            if dest_path.exists():
                raise FileExistsError(f'a file already exists at this path: {colored(dest_path,"red")}')
            # checking if the destination directory exists. and if not, creating it
            if not(dest_path_parent.exists()):
                #logging.info(f'creating directory: {colored(dest_path.parent,"red")}')
                dest_path_parent.mkdir(parents=True, exist_ok=True)

            #logging.debug(f'converting image to jpg')
            self.convert2jpg(dest_path, delete_org, source_img_path)


        except FileNotFoundError:
            #print(f'image file not found at this path: {colored(source_img_path,"red")}')
            result.add_result("image file not found at this path:")
        except UnidentifiedImageError:
            #print(f'file is not an image at path: {colored(source_img_path,"red")}')
            result.add_result("file is not an image at path:")
        except FileExistsError as e:
            #print(e)
            result.add_result(str(e)+"\n")
        except AlreadyJpgError as e:
            #print(e)
            result.add_result(str(e)+"\n")

        finally:
            if issubclass(self.image.__class__, Image.Image):
                #logging.debug(f'closing image {colored(source_img_path,"green")}')
                self.image.close()
            return None

    def convert2jpg(self, dest_path:Path, delete_org:bool, source_img_path:Path=None):
        self.image = self.image.convert('RGB')
        #logging.debug(f'saving image to {dest_path}')
        self.image.save(dest_path, 'JPEG')
        #print("source_image_path",source_img_path)
        result.add_result("Image convert successful:"+str(source_img_path))
        if delete_org:
            #print(colored(f'deleting original image at {source_img_path}', 'red'))
            result.add_result("deleting original image at")
            remove_file(source_img_path)
        return None

def convert_func(org_images_dir_path_str, dest_dir_input_str, delete_org_input):
    result.draw_Dialog(1)
    if delete_org_input == 'Y':
        delete_org = True
        #print(colored('original images will be deleted', 'red'))
        result.add_result("original images will be deleted")
    else:
        delete_org = False
    if len(dest_dir_input_str) == 0:
        dest_dir_path = None
    else:
        dest_dir_path = dest_dir_input_str.strip()
    org_images_dir_path = Path().cwd() / org_images_dir_path_str
    images_paths = [img_path for img_path in org_images_dir_path.iterdir() if (img_path.is_file() and img_path.suffix.lower() in ['.jpg','.jpeg','.png','.gif','.tiff'])]

    for image_path in images_paths:
        try:
            result.add_result(str(image_path))
            JpgConverter(source_img_path=image_path, dest_dir=dest_dir_path, delete_org=delete_org)
        except AlreadyJpgError as e:
            #print(e)
            result.add_result(str(e))

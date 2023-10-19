import image_downloader
import xlsx_reader
import json
#from time import sleep
import result

def downloader_func(input_xlsx_file_str, save_dir_str):
    try:
        save_dir = image_downloader.get_save_directory(save_dir_str)
        pylight_db = xlsx_reader.get_pylight_database(input_xlsx_file_str)
    except FileNotFoundError as e:
        print(type(e).__name__, e)
        result.add_result(json.dumps(str(e)))
    except xlsx_reader.MoreThanOneSheetError as e:
        print(type(e).__name__, e)
        result.add_result(json.dumps(str(e)))
    except xlsx_reader.FileNot_XLSX_Error as e:
        print(type(e).__name__, e)
        result.add_result(json.dumps(str(e)))
    image__names_urls_dict = xlsx_reader.read_data_from_xlsx(pylight_db)
    download(image__names_urls_dict,save_dir)

def download(image__names_urls_dict,save_dir):
    result.draw_Dialog(3)
    for image_name, image_url in image__names_urls_dict.items():
        try:
            response_status, response = image_downloader.download_image(image_url)
            if response_status == 403:
                for i in range(2):
                    response_status, response = image_downloader.download_image(image_url)
                    if response_status == 200:
                        result.add_result("download successful" + image_url + "\n")
                        break
                if response_status == 403:
                    raise image_downloader.cantDownloadImage(f'Error downloading image from: {image_url}, status code: {response_status}')
                    result.add_result("Error downloading image from:")
            image_downloader.check_image_exists(save_dir, image_name)
            image_save_path = image_downloader.touch_image_file(save_dir, image_name)
            image_downloader.save_image_to_file(response, image_save_path)
        except image_downloader.cantDownloadImage as e:
            print(str(e))
            result.add_result(json.dumps(str(e)))
            #add_result(e)
        except image_downloader.imageAlreadyExistsError as e:
            print(str(e))
            result.add_result(json.dumps(str(e)))
    #add_result(value)
#if __name__ == '__main__':



import os
import shutil
import asyncio

from APIs.YouTube.Downloader import YTLData


class FileOperationsOS:
    def change_dir():
        os.chdir("Music")


    def os_rename():
        try:
            print(os.listdir())
            file_name = os.rename(YTLData.get_data(), YTLData.video_info.get('title', None) + ".mp4")
        except FileExistsError:
            pass


    def create_folder(folder_name):
        try:
            os.chdir(folder_name)
        except FileNotFoundError:
            os.mkdir(folder_name)
            os.chdir(folder_name)
        return folder_name


    def read_dir():
        for f in os.listdir("."):
            return f[YTLData.title() + ".mp4"]

            
    def move_file():
        asyncio.sleep(3)
        shutil.move(FileOperationsOS.read_dir(), "Music")
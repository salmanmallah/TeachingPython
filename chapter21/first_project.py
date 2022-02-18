"""
    CHAPTER NO 21
    TUTORIAL NO. 231
    FILE SEPARATOR APPLICATION
    Python Project One
    By: SALMAN MALLAH
"""
import os
import shutil

os.chdir(r'C:\Users\CCS\OneDrive\Desktop\Separate files')
path = r'C:\Users\CCS\OneDrive\Desktop\Separate files'

dict_extension = {
    'picture_extensions': ('.png', '.jpg', '.jpeg'),
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'document_extension': ('.docx', '.pdf', '.txt', '.log', '.LOG'),
    'video_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg', '.webm')
}


def file_finder(folder_path, file_extension):
    files = []
    for file in os.listdir(folder_path):
        if file.endswith(file_extension):
            files.append(file)
    return files


for extension_type, extension_value in dict_extension.items():
    # print(file_finder(path, extension_value))
    folder_name = extension_type.split("_")[0].title() + ' File'
    folder_path = os.path.join(path, folder_name)
    # os.mkdir(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    for item in file_finder(path, extension_value):
        item_path = os.path.join(path, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path, item_new_path)

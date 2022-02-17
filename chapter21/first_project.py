"""
    CHAPTER NO 21
    TUTORIAL NO. 231
    FILE SEPARATOR APPLICATION
    Python Project One
    By: SALMAN MALLAH
"""
import os
import shutil

os.chdir(r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials')
path = r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials'

dict_extension = {
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extension': ('.docx', '.pdf', '.txt')
}


def file_finder(folder_path, file_extension):
    files = []
    for file in os.listdir(folder_path):
        if file.endswith(file_extension):
            files.append(file)
    return files


for key, value in dict_extension.items():
    print(file_finder(path,value))
# for extension_type, extension_value in dict_extension.items():
#     print(f'Calling file_finder ...')
#     print(file_finder(path, extension_value))

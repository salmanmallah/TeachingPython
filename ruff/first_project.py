import os
import shutil

os.chdir(r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials')
path = r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials'

dict_extension = {
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'document_extension': ('.docx', '.pdf', '.txt'),
    'video_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg')
}


def file_finder(folder_path, file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files


# print(file_finder(path, ('.mp3', '.m4a', '.wav', '.flac')))
for file_name, file_extension in dict_extension.items():
    # output = file_finder(path, file_extension)
    folder_name = file_name.split("_")[0].title() + " File"
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_name, exist_ok=True)
    for item in file_finder(path, file_extension):
        item_path = os.path.join(path, file_extension)
        print(item_path)
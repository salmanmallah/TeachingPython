import os
import shutil

os.chdir(r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials')
path = r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials'

dict_extension = {
    'picture_extensions': ('.png', '.jpg', '.jpeg'),
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'document_extension': ('.docx', '.pdf', '.txt', '.LOG'),
    'video_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg', '.webm'),
    'zip_extensions': ('.rar',)
}


def file_finder(folder_path, file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files


for extension_type, extension_value in dict_extension.items():
    # output = file_finder(path, file_extension)
    folder_name = extension_type.split("_")[0].title() + " File"
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_name, exist_ok=True)

    for item in file_finder(path, extension_value):
        item_path = os.path.join(path, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path, item_new_path)

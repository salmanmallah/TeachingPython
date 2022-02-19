import os
import shutil
# Programmed by: Salman Mallah
os.chdir(r"C:\Users\CCS LAPTOP HYD\Desktop\python tutorials")
path = r'C:\Users\CCS LAPTOP HYD\Desktop\python tutorials'
dictionary = {
    'photos': ('.png', '.jpg', '.jpeg'),
    'audios': ('.mp3', '.m4a', '.wav', '.flac'),
    'documents': ('.docx', '.pdf', '.txt', '.LOG', '.rar'),
    'videos': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg', '.webm'),

}

for file, extension in dictionary.items():
    make_folder = file.title() + ' File'
    os.makedirs(make_folder, exist_ok=True)
    destination_folder = os.path.join(path, make_folder)

    for data in os.listdir(path):
        if data.endswith(extension):
            target = os.path.join(path, data)
            shutil.move(target, destination_folder)

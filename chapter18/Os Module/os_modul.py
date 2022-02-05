"""
    CHAPTER NO. 18
    TUTORIAL NO. 228
    OS MODULE
"""
import os
# print(os.getcwd())
os.mkdir('subfolder')
# os.rmdir('subfolder')
# print(os.path.exists('subfolder'))

# check that folder is exists or not
if os.path.exists('subfolder'):
    print('Folder is already created')
else:
    # if not present than create below folder
    os.mkdir('subfolder')
"""
    CHAPTER NO. 18
    TUTORIAL NO. 228
    OS MODULE
"""
import os
# print(os.getcwd())
# os.mkdir('subfolder')
# os.rmdir('subfolder')
# print(path.exists('Movies'))

# check that folder is exists or not
# if path.exists('Movies'):
#     print('Folder is already created')
# else:
#     # if not present than create below folder
#     mkdir('Movies')
#
# # rmdir('Movies')
# print(path.exists('Movies'))

# to create file
# open('uncreate.txt', 'a').close()

# to delete file
# os.remove('uncreate.txt')

# to change dir
os.chdir('..')
print(os.listdir())

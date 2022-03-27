""" CHAPTER NO. 18
    TUTORIAL NO 219 | 220 | 221
    TEST
    logic:
        page = '<a href="www.facebook.com">facebook</a>'
        pos = page.find('<a href=')
        ffind = page.find('"', pos)
        lfind = page.find('"', ffind+1)
        print(page[ffind+1:lfind])
"""
# with open('index.html', 'r') as webpage:
#     with open('output.txt', 'a') as output:
#         for line in webpage.readlines():
#             if "<a href=" in line:
#                 ffind = line.find('<a href=')
#                 first_qoute = line.find('\"', ffind)
#                 second_qoute = line.find('\"', first_qoute+1)
#                 url = line[first_qoute+1:second_qoute]
#                 output.write(f'{url}\n')

"""Tutorial no. 221 starts from here
    Better solution for test two
    Programmer: Salman    
"""
with open('index.html', 'r') as webpage:
    with open('output.txt', 'w') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_qoute = page.find('"', pos)
                second_qoute = page.find('"', first_qoute + 1)
                url = page[first_qoute + 1:second_qoute]
                wf.write(f'{url}\n')
                page = page[second_qoute:]

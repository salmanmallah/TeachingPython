"""
    CHAPTER NO. 18
    TUTORIAL NO 219 | 220
    TEST TWO
"""
with open('index.html', 'r') as webpage:
    with open('output.txt', 'a') as output:
        for line in webpage.readlines():
            if "<a href=" in line:
                ffind = line.find('<a href=')
                first_qoute = line.find('\"', ffind)
                second_qoute = line.find('\"', first_qoute+1)
                url = line[first_qoute+1:second_qoute]
                output.write(f'{url}\n')
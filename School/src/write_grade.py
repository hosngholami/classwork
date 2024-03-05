import os
def write_grade(file):
        
    path_file = os.getcwd() + '/School/data/book.json'
    with open(path_file, 'w') as file:
        file.write('test')

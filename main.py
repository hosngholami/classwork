from source.add import add
from source.sub import sub
from ZOO.bird import Bird
from School.src.insert_grade import insert_grade
from School.src.write_grade import write_grade
import os


import numpy as np
import pandas as pd

def main():
    # add_number = add(1, 2, 3, 4, 5)
    # sub_number = sub(1, 2, 3, 4, 5)

    # type_animal_dict = {
    #     1: 'khazandeh',
    #     2: 'parandeh'
    # }

    # print(type_animal_dict)
    # type_animal = input("enter type animal: ")
    # name = input("enter name animal: ")


    # bird = Bird(type=type_animal, name=name)
    # print(bird.fly())


    # return (add_number, sub_number)

    # lecture = insert_grade()
    # write_grade(lecture)

    l = np.array([['1', '2', '3', '4'], 
                  ['5', '6', '7', '8']
                  ])
    

    path = os.getcwd() + '/data/INFO.csv'

    data = pd.read_csv(path)


    print(data)
    return l[0, 3]







print(main())